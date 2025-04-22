
<!-- my-python-project/ # Renamed root
├── app_cron/          # Original CronJob app
│   ├── main.py
│   └── requirements.txt
├── app_grpc/          # New gRPC service app
│   ├── protos/
│   │   └── service.proto     # Protocol buffer definition
│   ├── service_pb2.py      # Generated code
│   ├── service_pb2_grpc.py # Generated code
│   ├── server.py           # gRPC server implementation
│   └── requirements.txt    # gRPC dependencies
├── k8s/
│   ├── cronjob.yaml
│   ├── grpc-deployment.yaml # New
│   └── grpc-service.yaml    # New
├── helm/                  # Optional Helm Chart (needs updates)
│   └── my-python-project/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── templates/
│       │   ├── _helpers.tpl
│       │   ├── cronjob.yaml
│       │   ├── grpc-deployment.yaml # New template
│       │   └── grpc-service.yaml    # New template
│       └── .helmignore
├── cron.Dockerfile        # Dockerfile for the CronJob
├── grpc.Dockerfile        # Dockerfile for the gRPC service
└── README.md              # Needs significant updates -->

### Generate python grpc bindings
```
brew install protobuf
pip install grpcio-tools

python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/service.proto
```
