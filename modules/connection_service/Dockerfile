FROM python:3.8

WORKDIR /opt/connection-service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5006

COPY . .

ENV PYTHONPATH /opt/connection-service

# compile protobuf classes
RUN python -m grpc_tools.protoc -Iapp/proto --python_out=. --grpc_python_out=. app/proto/PersonMessage.proto
RUN python -m grpc_tools.protoc -Iapp/proto --python_out=. --grpc_python_out=. app/proto/ConnectionMessage.proto
CMD ["python", "start.py"]