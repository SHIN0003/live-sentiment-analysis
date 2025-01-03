# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port Streamlit will run on
EXPOSE 1000

# Run the Streamlit application
CMD ["streamlit", "run", "/app/dashboard.py", "--server.port=1000", "--server.address=0.0.0.0"]
