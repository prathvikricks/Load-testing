# Base image for Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY ./code/test_app.py /app/
COPY ./code/requirements.txt /app/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask app
EXPOSE 5000

# Start the Flask app
CMD ["python", "test_app.py"]
