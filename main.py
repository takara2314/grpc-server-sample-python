import random as rand
from concurrent import futures
import grpc
import dice_pb2_grpc
import dice_pb2

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

class DiceServicer(dice_pb2_grpc.DiceServiceServicer):
    def RollDice(self, request, context):
        random_num = rand.randint(
            request.min_num,
            request.max_num
        )

        return dice_pb2.RollDiceResponse(
            result=random_num
        )

def main():
    dice_pb2_grpc.add_DiceServiceServicer_to_server(DiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("start gRPC server port: 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        server.stop(0)
        print("stopping gRPC server...")
