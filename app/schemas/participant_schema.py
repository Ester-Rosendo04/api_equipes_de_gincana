from app.extensions import ma
from app.models.participant import Participant
from marshmallow import validate, fields
from marshmallow_sqlalchemy import auto_field

fields.Field.default_error_messages["required"] = "Campo obrigatório"

class ParticipantSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Participant

    id = auto_field(dump_only=True)

    nome = auto_field(
        required=True,
        validate=validate.Length(min=1, max=255)
    )
    idade = auto_field(
        required=True,
        validate=validate.Range(min=10, max=100)
    )
    team_id = auto_field(
        required=True,
        validate=validate.Range(min=1)
    )
