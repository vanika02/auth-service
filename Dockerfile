# Use Python base image
FROM python:3.10-slim


# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# Expose port
EXPOSE 8000

# Run server
CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"