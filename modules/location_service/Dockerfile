FROM python:3.8

WORKDIR /opt/location-service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5003

ENV PYTHONPATH /opt/location-service

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "-p", "5003"]