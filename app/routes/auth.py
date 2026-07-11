from flask import Blueprint, jsonify, request
from app.controllers.auth_controller import entrar

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/login")
def login():
    data = request.get_json()
    data, status = entrar(data)
    return jsonify(data), status
