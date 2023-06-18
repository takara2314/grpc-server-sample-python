# gRPC Server Sample Python

サイコロの値を返すgRPCサーバーのサンプル (Python版)

[参考サイト](https://qiita.com/ny7760/items/1c793e7cd651c4c9e449)

## 開発環境の構築

1. Protocol Bufferをインストール
   [https://github.com/protocolbuffers/protobuf/releases](https://github.com/protocolbuffers/protobuf/releases)

2. grpcio-tools をインストール

```shell
pip install grpcio-tools
```

## コード生成

```shell
python codegen.py
```

## クライアントのサンプル

[https://github.com/takara2314/grpc-client-sample](https://github.com/takara2314/grpc-client-sample)
