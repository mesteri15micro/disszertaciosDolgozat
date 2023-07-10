# Use the official Python image as the base image
FROM python:3.10

# Install necessary packages
RUN apt-get update && apt-get install -y \
    xvfb \
    x11-xserver-utils \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

LABEL author="Berecki Zoltan"
LABEL description="Mesteri disszertacios dolgozathoz alkalmazas"
LABEL version="1.0"

# Copy all the Python program files to the container
COPY Custom_UIP_ver04.py .
COPY binpackingVisualization.py .
COPY Cristofides_Visualization.py .
COPY graphColoringVisualization.py .
COPY hamiltonCircleVisualization.py .
COPY knapsackVisualization.py .
COPY TSP_Visualization.py .
COPY dodekaeder.py .
COPY CNF_SatisfiabilityVisualization.py .
COPY parhuzamosProgramozasNPTeljesFeladatokra4.py .

# Install Python dependencies
RUN pip install --no-cache-dir \
    matplotlib \
    numpy \
    networkx

# Set environment variables for Xvfb
ENV DISPLAY=:99

# Set the entry point command to run Xvfb and the Python program
CMD Xvfb :99 -screen 0 1024x768x16 & \
    sleep 1 && \
    python Custom_UIP_ver04.py
