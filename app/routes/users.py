from flask import Blueprint, request
from app.controllers.user_controller import cadastrar, listar_usuarios

users_bp = Blueprint("users", __name__)

@users_bp.get("/")
def get_users():
    data, status = listar_usuarios()
    return data, status

@users_bp.post("/register")
def register():
    data = request.get_json()
    data, status = cadastrar(data)
    return data, status
