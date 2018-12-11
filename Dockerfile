FROM python:alpine

WORKDIR /app
COPY requirements.txt .
COPY service_discovery_test.py .

RUN pip install -r requirements.txt
ENTRYPOINT python service_discovery_test.py