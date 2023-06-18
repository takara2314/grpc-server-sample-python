import os
from grpc.tools import protoc

os.chdir("./proto")

protoc.main(
    (
        "-I .",
        "--python_out=..",
        "--grpc_python_out=..",
        "*",
    )
)

os.chdir("../")
