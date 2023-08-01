FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY scale_service.py scale_service.py

CMD ["python", "scale_service.py"]

