from app.models.user import User
from app.utils.response import error_response, success_response
from flask_jwt_extended import create_access_token
import bcrypt

def entrar(data):
    if not "email" in data or not "password" in data:
        return error_response("Email e senha são obrigatórios", 400)

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return error_response("Usuário não encontrado", 404)
    
    senha_digitada = data["password"]

    if not bcrypt.checkpw(
        senha_digitada.encode("utf-8"),
        user.password.encode("utf-8")
    ):
        return error_response("Senha incorreta", 401)

    access_token = create_access_token(identity=str(user.id))

    return success_response({"access_token": access_token})
