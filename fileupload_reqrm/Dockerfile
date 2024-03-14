# Use the official Python image as a base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Define environment variables
ENV FLASK_APP=""uploadfile.py""
ENV FLASK_RUN_HOST="0.0.0.0"

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
