from flask import Blueprint, jsonify, request
from app.controllers.team_controller import listar_equipes, criar_equipe, atualizar_equipe, deletar_equipe
from app.controllers.participant_controller import listar_participantes_por_equipe
from flask_jwt_extended import jwt_required

teams_bp = Blueprint("teams", __name__)

@teams_bp.route("/", methods=["GET"])
def get_teams():
    data, status = listar_equipes()
    return jsonify(data), status

@teams_bp.route("/", methods=["POST"])
@jwt_required()
def create_team():
    data = request.get_json()
    data, status = criar_equipe(data)
    return jsonify(data), status

@teams_bp.route("/<int:team_id>/participants", methods=["GET"])
def get_team_participants(team_id):
    data, status = listar_participantes_por_equipe(team_id)
    return jsonify(data), status

@teams_bp.route("/<int:team_id>", methods=["PATCH"])
@jwt_required()
def update_team(team_id):
    data = request.get_json()
    data, status = atualizar_equipe(team_id, data)
    return jsonify(data), status

@teams_bp.route("/<int:team_id>", methods=["DELETE"])
@jwt_required()
def delete_team(team_id):
    _, status = deletar_equipe(team_id)
    return "", status
