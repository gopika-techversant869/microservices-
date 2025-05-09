import wallet_pb2
import wallet_pb2_grpc
from db.models import Wallet
from datetime import datetime
from db.db_config import db
import grpc
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WalletService(wallet_pb2_grpc.WalletServiceServicer):
    def CreateWallet(self, request, context):
        """
        Handles wallet creation for a user. If a wallet already exists, it returns the existing wallet.
        """
        try:
            existing_wallet = db.query(Wallet).filter_by(user_id=request.user_id).first()
            if existing_wallet:
                logger.info(f"Wallet already exists for user_id: {request.user_id}")
                return wallet_pb2.WalletResponse(
                    wallet_id=str(existing_wallet.id),
                    status="already_exists"
                )

            new_wallet = Wallet(
                user_id=request.user_id,
                card_id=request.card_number,
                status="active",
                created_at=datetime.utcnow(),
                activated_at=datetime.utcnow()
            )
            db.add(new_wallet)
            db.commit()

            logger.info(f"New wallet created with ID: {new_wallet.id} for user_id: {request.user_id}")
            return wallet_pb2.WalletResponse(
                wallet_id=str(new_wallet.id),
                status="created"
            )
        except Exception as e:
            db.rollback()
            logger.error(f"Error creating wallet for user_id: {request.user_id} - {str(e)}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return wallet_pb2.WalletResponse()
        finally:
            db.close()

class TestService(wallet_pb2_grpc.TestServiceServicer):
    def test(self, request, context):
        """
        A simple test function to verify service functionality.
        """
        logger.info(f"Test function called with request type: {type(request)}")
        return wallet_pb2.TestResponse(
            message="It's a test function"
        )