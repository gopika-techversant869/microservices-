import logging
from datetime import datetime

from app.db.db_common_services import DBService
from app.models.card_model import User
from app.models.card_model import Card
import logging
from flask import jsonify
from app.messaging.publisher import QueueService




class CardServiceImpl:

    def __init__(self):

        self.db_obj = DBService()
        self.queue = QueueService()

    def card_creation(self,request):

        logging.info("Card creation request received",request)

        existing_user = self.db_obj.find_one(User, {"user_id": request.user_id})
        if not existing_user:
            return jsonify({"error": "User not found"}), 404
        
        card_data = {
            "card_number": request.card_number,
            "status":"pending",
            "expiry_date": request.expiry_date,
            "created_at":datetime.utnow(),
            "card_type": request.card_type,
            "card_last_digits": request.card_last_digits,
            "card_network": request.card_network,
            "card_variant": request.card_variant,
            "user_id": request.user_id
        }
        
        card_details = self.db_obj.create_record(Card,card_data)
        card_details = self.db_obj.create_record(Card, card_data)

        wallet_payload = {
            "user_id": request.user_id,
            "card_id": card_details.id,
            "card_number": request.card_number
        }

        self.queue.publish_wallet_creation(wallet_payload)

        return jsonify({"message": "Card created and wallet creation triggered", "card_id": card_details.id}), 201


