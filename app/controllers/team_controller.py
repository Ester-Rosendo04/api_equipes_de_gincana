from app.extensions import db
from app.models.team import Team
from app.utils.response import success_response, error_response
from app.schemas.team_schema import TeamSchema

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)

def listar_equipes():
    equipes = Team.query.all()
    return success_response(teams_schema.dump(equipes))

def criar_equipe(data):

    dados_validados = team_schema.load(data)
    novo_time = Team(**dados_validados)

    db.session.add(novo_time)
    db.session.commit()

    return success_response(team_schema.dump(novo_time), 201)
