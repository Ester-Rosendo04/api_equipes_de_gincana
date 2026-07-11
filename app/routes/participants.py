from flask import Blueprint, jsonify, request
from app.controllers.participant_controller import (
  listar_participantes,
  criar_participante,
  atualizar_participante,
  deletar_participante,
)
from flask_jwt_extended import jwt_required

participants_bp = Blueprint("participants", __name__)

@participants_bp.route("/", methods=["GET"])
def get_participants():
    data, status = listar_participantes()
    return jsonify(data), status

@participants_bp.route("/", methods=["POST"])
@jwt_required()
def create_participant():
    data = request.get_json()
    data, status = criar_participante(data)
    return jsonify(data), status

@participants_bp.route("/<int:participant_id>", methods=["PATCH"])
@jwt_required()
def update_participant(participant_id):
    data = request.get_json()
    data, status = atualizar_participante(participant_id, data)
    return jsonify(data), status

@participants_bp.route("/<int:participant_id>", methods=["DELETE"])
@jwt_required()
def delete_participant(participant_id):
    _, status = deletar_participante(participant_id)
    return "", status
