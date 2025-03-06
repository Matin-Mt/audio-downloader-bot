# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (if needed)
# For example, you can specify the environment variables for MongoDB, etc.
# ENV MONGO_HOST=your_mongo_host
# ENV MONGO_USER=your_mongo_user

# Expose port for your app (if needed)
EXPOSE 5000

# Run your bot application
CMD ["python", "src/main.py"]
