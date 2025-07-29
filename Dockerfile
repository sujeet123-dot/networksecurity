FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Install awscli and Python dependencies
RUN apt-get update -y && \
    apt-get install -y awscli && \
    pip install --no-cache-dir -r requirement.txt

CMD ["python3", "app.py"]
