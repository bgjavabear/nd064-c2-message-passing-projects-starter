FROM python:3.8

WORKDIR /opt/control-service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

ENV PYTHONPATH /opt/control-service

# compile protobuf classes
RUN python -m grpc_tools.protoc -Iapp/control_service/proto --python_out=. --grpc_python_out=. app/control_service/proto/PersonMessage.proto
RUN python -m grpc_tools.protoc -Iapp/control_service/proto --python_out=. --grpc_python_out=. app/control_service/proto/ConnectionMessage.proto
CMD ["flask", "run", "--host", "0.0.0.0"]