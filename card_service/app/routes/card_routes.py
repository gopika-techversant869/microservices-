from flask import Blueprint, request, jsonify
from app.services.card_service import create_card

card_bp = Blueprint('card', __name__)

@card_bp.route('/card/creation', methods=['POST'])
def create_card_route():
    data = request.json
    # user_id = data.get('user_id')
    # if not user_id:
    #     return jsonify({"error": "user_id is required"}), 400
    # card = create_card(user_id)
    # return jsonify({
    #     "id": card.id,
    #     "user_id": card.user_id,
    #     "card_number": card.card_number,
    #     "status": card.status,
    #     "created_at": card.created_at
    # }), 201
