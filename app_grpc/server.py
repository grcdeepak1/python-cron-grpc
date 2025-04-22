# app_grpc/server.py
import grpc
from concurrent import futures
import time
import logging

# Import generated classes
import service_pb2
import service_pb2_grpc

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Implement the service class based on the generated Servicer
class GreeterServicer(service_pb2_grpc.GreeterServicer):
    """Provides methods that implement functionality of greeter server."""

    def SayHello(self, request, context):
        """Handles the SayHello RPC request."""
        logging.info(f"Received SayHello request for name: {request.name}")
        # Basic validation or logic can go here
        if not request.name:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Name cannot be empty")
            return service_pb2.HelloReply()

        message = f"Hello, {request.name}!"
        logging.info(f"Sending reply: {message}")
        return service_pb2.HelloReply(message=message)

def serve():
    """Starts the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # Listen on port 50051. Use 0.0.0.0 to accept connections from any IP within the pod network.
    port = "50051"
    server.add_insecure_port(f'[::]:{port}') # Supports IPv4 and IPv6

    logging.info(f"Starting gRPC server on port {port}")
    server.start()
    logging.info("Server started. Waiting for requests...")

    # Keep the server running indefinitely
    try:
        while True:
            time.sleep(86400) # Sleep for a day; server runs until interrupted
    except KeyboardInterrupt:
        logging.info("Server shutting down...")
        server.stop(0) # Graceful shutdown

if __name__ == '__main__':
    serve()