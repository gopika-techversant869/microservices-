from flask import Flask, request, jsonify
import grpc
import wallet_pb2
import wallet_pb2_grpc

app = Flask(__name__)

# channel = grpc.insecure_channel('localhost:50051')
# stub = wallet_pb2_grpc.WalletServiceStub(channel)

@app.route('/wallet/balance', methods=['GET'])
def get_balance():
    # user_id = request.args.get("user_id")
    # req = wallet_pb2.GetBalanceRequest(user_id=user_id)
    # res = stub.GetBalance(req)
    return jsonify({"balance": 1000})

if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=5002)

