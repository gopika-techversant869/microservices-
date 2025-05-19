from flask import Blueprint, request, jsonify
from app.services.card_service import CardServiceImpl
from app.services.card_service import TestService

card_bp = Blueprint('card', __name__)

@card_bp.route('/card/creation', methods=['POST'])
def create_card_route():
    data = request.json
    print(":data:::::::::::::::::::::::::::::::::::",data)
    card_obj = CardServiceImpl()
    return card_obj.card_creation(data)
# return jsonify({"message": "Card created and wallet creation triggered", "card_id": ""}), 201

@card_bp.route('/test', methods=['GET'])
def test_route():
    print("test route")
    test_obj = TestService()
    return test_obj.test_service()