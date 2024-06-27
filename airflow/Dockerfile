FROM apache/airflow:2.9.1

# Switch to root to install system dependencies
USER root

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       pkg-config \
       libhdf5-dev \
       gcc \
       python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch to airflow user to install Python packages
USER airflow

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
