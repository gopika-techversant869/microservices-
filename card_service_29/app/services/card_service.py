import logging
from datetime import datetime
import logging
from flask import jsonify
from app.client_service import create_wallet
from app.db.models import User
from app.db.models  import Card
from app.db.db_handler import db





class CardServiceImpl:

    def __init__(self):
        pass


    def card_creation(self,request):
        print("request::::::::::::;",request)

        logging.info("Card creation request received",request)

        # existing_user = self.db_obj.find_one(User, {"user_id": request.get('user_id')})
    
        existing_user = User.query.filter_by(user_id = request.get('user_id')).first()
        print("existing user:::::::::::::", existing_user)
     
        if not existing_user:
            return jsonify({"error": "User not found"}), 404
        
        # card_data = {
        #     "card_number": request.get('card_number'),
        #     "status":"pending",
        #     "expiry_date": request.get('expiry_date'),
        #     "created_at":datetime.utcnow(),
        #     "card_type": request.get('card_type'),
        #     "card_network": request.get('card_network'),
        #     "card_variant": request.get('card_variant'),
        #     "user_id": request.get('user_id')
        # }
        try:
            new_user = Card(card_number = request.get('card_number'),
                            status = "pending",
                            expiry_date = request.get('expiry_date'),
                            created_at = datetime.utcnow(),
                            card_type =  request.get('card_type'),
                            card_network =  request.get('card_network'),
                            card_variant =  request.get('card_variant'),
                            # Add and commit the new user
            user_id =  request.get('user_id') )

            db.add(new_user)
            db.commit()
        except Exception as e:
            print("eeee",e)

        # card_details = self.db_obj.create_record(Card,card_data)
        # print("card details:::::::::::::",card_details)
        

        # wallet_payload = {
        #     "user_id": request.get('user_id'),
        #     "card_id": new_user.id,
        #     "card_number": request.get('card_number')
        # }

        # self.queue.publish_wallet_creation(wallet_payload)
        wallet = create_wallet(request.get('user_id'), new_user.id)
        print("wallet:::::::::::::", wallet)


        return jsonify({"message": "Card created and wallet creation triggered", "card_id": new_user.id}), 201


