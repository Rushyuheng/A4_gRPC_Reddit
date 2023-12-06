python -m grpc_tools.protoc -I ./protobuf --python_out=./src/gen --pyi_out=./src/gen --grpc_python_out=./src/gen ./protobuf/model.proto ./protobuf/service.proto 
