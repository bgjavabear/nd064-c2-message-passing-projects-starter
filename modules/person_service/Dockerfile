FROM python:3.8

WORKDIR /opt/person-service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .

ENV PYTHONPATH /opt/person-service

# compile protobuf classes
RUN python -m grpc_tools.protoc -Iapp/proto --python_out=. --grpc_python_out=. app/proto/PersonMessage.proto
CMD ["python", "start.py"]