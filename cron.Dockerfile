# Dockerfile

# 1. Choose a base Python image
FROM python:3.9-slim

# 2. Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy requirements first to leverage Docker cache
COPY app_cron/requirements.txt .

# 5. Install dependencies
#    --no-cache-dir: Reduces image size by not storing the pip cache
#    --trusted-host pypi.python.org: Can sometimes help avoid SSL issues in certain environments
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# 6. Copy the rest of the application code
COPY app_cron/ .

# 7. Define the command to run when the container starts
#    This will execute `python main.py`
CMD ["python", "main.py"]