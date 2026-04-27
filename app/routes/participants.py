from flask import Blueprint, jsonify, request
from app.controllers.participant_controller import listar_participantes, criar_participante

participants_bp = Blueprint("participants", __name__)

@participants_bp.route("/", methods=["GET"])
def get_participants():
    data, status = listar_participantes()
    return jsonify(data), status

@participants_bp.route("/", methods=["POST"])
def create_participant():
    data = request.get_json()
    data, status = criar_participante(data)
    return jsonify(data), status
