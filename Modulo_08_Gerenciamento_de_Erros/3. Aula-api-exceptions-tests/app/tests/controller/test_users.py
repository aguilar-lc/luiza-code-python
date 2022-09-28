
from pytest import fixture, raises, mark
from fastapi.exceptions import HTTPException

from app.server.controller.users import UserController
from app.server.models.users import UserSchema


@fixture
def user_controller():
    return UserController()

def test_valida_usuario_success(user_controller):
    user = UserSchema(
        name="Michelly Alves",
        age=18,
        cpf="0000000",
        email="michellydsalves@gmail.com"
    )
    
    result = user_controller.add_user(user)
    assert result == True
