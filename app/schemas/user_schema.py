from app.extensions import ma
from app.models.user import User
from marshmallow import validate, fields
from marshmallow_sqlalchemy import auto_field

fields.Field.default_error_messages["required"] = "Campo obrigatório"

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = auto_field(dump_only=True)

    email = auto_field(
        required=True,
        validate=validate.Length(min=1, max=100)
    )
    password = auto_field(
        required=True,
        validate=validate.Length(min=6, max=255),
        load_only=True
    )
