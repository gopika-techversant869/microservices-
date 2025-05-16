FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose both HTTP and gRPC ports
EXPOSE 5002 50051

# Default command (can be overridden in Kubernetes)
CMD ["python", "http_adapter.py"]