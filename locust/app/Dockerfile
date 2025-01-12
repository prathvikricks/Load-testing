# Base image for Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /load_testing

# Copy Locust test files
COPY ./code/locustfile.py /load_testing/

# Install Locust
RUN pip install --no-cache-dir locust

# Expose port for Locust web interface
EXPOSE 8089

# Run Locust
CMD ["locust", "-f", "locustfile.py", "--host=http://app:5000"]
