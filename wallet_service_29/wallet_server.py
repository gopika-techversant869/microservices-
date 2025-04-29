import grpc
from concurrent import futures
import wallet_pb2_grpc
from services.wallet_handler import WalletService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    wallet_pb2_grpc.add_WalletServiceServicer_to_server(WalletService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("WalletService running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
