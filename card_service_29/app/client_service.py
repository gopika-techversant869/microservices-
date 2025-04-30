import grpc
import wallet_pb2
import wallet_pb2_grpc


def create_wallet(user_id, card_id):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = wallet_pb2_grpc.WalletServiceStub(channel)
        req = wallet_pb2.WalletRequest(
            user_id=str(user_id),
            card_number=str(card_id)
        )
        print("req", req)
        res = stub.CreateWallet(req)
    return res.wallet_id, res.status