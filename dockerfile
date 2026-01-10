FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (BEST PRACTICE)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy rest of application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
