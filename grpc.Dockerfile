# --- Builder Stage ---
FROM python:3.9-slim AS builder

WORKDIR /build

COPY app_grpc/requirements-build.txt .
RUN pip install --no-cache-dir -r requirements-build.txt

# Copy only the .proto files first
COPY app_grpc/protos/ /build/protos/

# Generate the Python bindings into a specific output directory
RUN mkdir /build/generated && \
	python -m grpc_tools.protoc \
	-I=/build/protos \
	--python_out=/build/generated \
	--grpc_python_out=/build/generated \
	/build/protos/service.proto

# --- Final Stage ---
FROM python:3.9-slim

WORKDIR /app

# Install only RUNTIME dependencies (not grpcio-tools)
# Make sure your requirements.txt includes 'grpcio' and 'protobuf'
COPY app_grpc/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy generated code from the builder stage
COPY --from=builder /build/generated /app/

# Copy your application code (that imports the generated code)
COPY app_grpc/ /app/

# Define runtime command (example)
CMD ["python", "server.py"]