import grpc
from concurrent import futures
import wallet_pb2_grpc
from services.wallet_handler import WalletService
from services.wallet_handler import TestService

def serve():
    print("Starting WalletService server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    wallet_pb2_grpc.add_WalletServiceServicer_to_server(WalletService(), server)
    wallet_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("WalletService running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


