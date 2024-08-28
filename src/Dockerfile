# Use the official Python image from the Docker Hub
FROM python:3.9 

# Label the image with metadata
LABEL maintainer="MIRI&RAN"

# Set the working directory in the container
WORKDIR /app

# Create the input-files directory
RUN mkdir -p /input-files

# Create the input-files directory
RUN mkdir -p /output-files

# Copy the current directory contents into the container at /app
COPY . .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app


# Set the entry point for the container
ENTRYPOINT ["python", "churn_prediction_pipeline/prediction_batch_pipeline.py"]

# Default command to provide flexibility if no arguments are passed
CMD ["--help"]


