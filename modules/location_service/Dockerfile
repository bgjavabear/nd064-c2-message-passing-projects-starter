FROM python:3.8

WORKDIR /opt/location-service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH /opt/location-service

COPY . .
CMD ["python", "start.py"]