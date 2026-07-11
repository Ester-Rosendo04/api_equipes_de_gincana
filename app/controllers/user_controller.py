import bcrypt
from app.extensions import db
from app.models.user import User
from app.utils.response import success_response
from app.schemas.user_schema import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def listar_usuarios():
    usuarios = User.query.all()
    return success_response(users_schema.dump(usuarios))

def cadastrar(data):
    senha = data["password"]

    # Gera o hash da senha
    senha_hash = bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    user = User(
        email=data["email"],
        password=senha_hash
    )

    db.session.add(user)
    db.session.commit()

    return success_response(user_schema.dump(user), 201)