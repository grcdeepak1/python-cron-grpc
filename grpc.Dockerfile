# grpc.Dockerfile

# 1. Base image
FROM python:3.9-slim

# 2. Environment variables
ENV PYTHONUNBUFFERED=1

# 3. Working directory
WORKDIR /app

# 4. Copy requirements first
COPY app_grpc/requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# 6. Copy application code (including protos and generated files)
COPY app_grpc/ /app/

# 7. Expose the gRPC port the server listens on
EXPOSE 50051

# 8. Command to run the server
CMD ["python", "server.py"]