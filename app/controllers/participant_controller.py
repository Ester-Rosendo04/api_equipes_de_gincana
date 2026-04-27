from app.extensions import db
from app.models.participant import Participant
from app.models.team import Team
from app.utils.response import success_response, error_response
from app.schemas.participant_schema import ParticipantSchema

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)

def listar_participantes():
    participantes = Participant.query.all()
    return success_response(participants_schema.dump(participantes))

def criar_participante(data):

    dados_validados = participant_schema.load(data)
    novo_participante = Participant(**dados_validados)
    team = Team.query.get_or_404(dados_validados["team_id"])

    db.session.add(novo_participante)
    db.session.commit()

    return success_response(participant_schema.dump(novo_participante), 201)

def listar_participantes_por_equipe(team_id):
    team = Team.query.get_or_404(team_id)

    participants = team.participants

    return success_response(participants_schema.dump(participants))
