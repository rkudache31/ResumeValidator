# Use the official Python image
FROM python:3.8

# Set the working directory in the container
#WORKDIR /app

# Set the OpenAI API key as an environment variable
ENV OPENAI_API_KEY="myaddedtestsk-TtN2pd19WpnAokeULuBpT3BlbkFJaimaN0siwQTK0i2bS64R"


# Copy the local requirements.txt file to the container
COPY requirements.txt .
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y \
    pkg-config \
    # Add any other necessary build dependencies here \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
#EXPOSE 8080
RUN pip install --no-cache-dir -r requirements.txt
# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "./resumeanalyzer.py"]

