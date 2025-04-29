import logging
from datetime import datetime

from app.db.db_common_services import DBService
from app.models.card_model import User
from app.models.card_model import Card
import logging
from flask import jsonify
from app.messaging.publisher import QueueService
from app.grpc_clients.wallet_client import create_wallet





class CardServiceImpl:

    def __init__(self):

        self.db_obj = DBService()
        self.queue = QueueService()

    def card_creation(self,request):
        print("request::::::::::::;",request)

        logging.info("Card creation request received",request)

        existing_user = self.db_obj.find_one(User, {"user_id": request.get('user_id')})
        if not existing_user:
            return jsonify({"error": "User not found"}), 404
        
        card_data = {
            "card_number": request.get('card_number'),
            "status":"pending",
            "expiry_date": request.get('expiry_date'),
            "created_at":datetime.utcnow(),
            "card_type": request.get('card_type'),
            "card_network": request.get('card_network'),
            "card_variant": request.get('card_variant'),
            "user_id": request.get('user_id')
        }
        
        card_details = self.db_obj.create_record(Card,card_data)
        print("card details:::::::::::::",card_details)

        wallet_payload = {
            "user_id": request.get('user_id'),
            "card_id": card_details.id,
            "card_number": request.get('card_number')
        }

        # self.queue.publish_wallet_creation(wallet_payload)
        wallet = create_wallet(request.get('user_id'), card_details.id)
        print("wallet:::::::::::::", wallet)


        return jsonify({"message": "Card created and wallet creation triggered", "card_id": card_details.id}), 201


