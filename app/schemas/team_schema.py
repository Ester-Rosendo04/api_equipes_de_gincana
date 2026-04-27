from app.extensions import ma
from app.models.team import Team
from marshmallow import validate, fields
from marshmallow_sqlalchemy import auto_field

fields.Field.default_error_messages["required"] = "Campo obrigatório"

class TeamSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Team

    id = auto_field(dump_only=True)

    nome = auto_field(
        required=True,
        validate=validate.Length(min=1, max=255)
    )
