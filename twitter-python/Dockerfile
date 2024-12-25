FROM python:3.11-slim
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
# Copy application files
COPY . .

# Use ENTRYPOINT for base command
ENTRYPOINT ["python"]

# Use CMD for default script
CMD ["main.py"]