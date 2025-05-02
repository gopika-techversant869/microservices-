import wallet_pb2, wallet_pb2_grpc
from db.models import Wallet
from datetime import datetime
from db.db_config import db
import grpc

class WalletService(wallet_pb2_grpc.WalletServiceServicer):

    def CreateWallet(self, request, context):
        print("request:::::::::::::::::::::::::::",type(request))
        print("user_id::::::::::::::::::",request.user_id)

        try:
 
            existing_wallet = db.query(Wallet).filter_by(user_id=request.user_id).first()
            print("existing_wallet::::::::::::::::::", existing_wallet)
            if existing_wallet:
                return wallet_pb2.WalletResponse(
                    wallet_id=str(existing_wallet.id),
                    status="already_exists"
                )
           
            new_wallet = Wallet(
                user_id=request.user_id,
                card_id=request.card_number,
                status = "active",
                created_at=datetime.utcnow(),
                activated_at=datetime.utcnow()
            )
            db.add(new_wallet)
            db.commit()
            print("new_wallet::::::::::::::::::", new_wallet.id)
            return wallet_pb2.WalletResponse(
                wallet_id=new_wallet.id,
                status="created"
            )
        except Exception as e:
            db.rollback()
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return wallet_pb2.WalletResponse()
        
        # except Exception as e:
        #     session.rollback()
        #     context.set_details(str(e))
        #     context.set_code(grpc.StatusCode.INTERNAL)
        #     return wallet_pb2.WalletResponse()
        # finally:
        #     session.close()

class TestService(wallet_pb2_grpc.TestServiceServicer):
    def test(self, request, context):
        print("request:::::::::::::::::::::::::::", type(request))
      
        return wallet_pb2.TestResponse(
           message = "Its a test function"
        )