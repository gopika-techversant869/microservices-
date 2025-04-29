from flask import Blueprint, request, jsonify
from app.services.card_service import CardServiceImpl

card_bp = Blueprint('card', __name__)

@card_bp.route('/card/creation', methods=['POST'])
def create_card_route():
    data = request.json
    print(":data:::::::::::::::::::::::::::::::::::",data)
    card_obj = CardServiceImpl()
    return card_obj.card_creation(data)
    
