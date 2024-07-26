# Use a base Ubuntu image
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    wget && \
    apt-get clean

# Copy the requirements.txt file into the container
COPY requirements.txt /app

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose Jupyter Notebook port
EXPOSE 8888

# Start Jupyter Notebook when the container runs
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
