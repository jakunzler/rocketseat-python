import pytest
from .jwt_handler import JwtHandler

def test_create_jwt_token():
    jwt_handler = JwtHandler()

    body = {
        "username": "olaMundo",
        "aqui": "estou aqui",
        "lalala": ""
    }

    token = jwt_handler.create_jwt_token(body)
    
    assert token is not None
    assert isinstance(token, str)

def test_decode_jwt_token():
    jwt_handler = JwtHandler()

    body = {
        "username": "olaMundo",
        "aqui": "estou aqui",
        "lalala": ""
    }

    token = jwt_handler.create_jwt_token(body)
    token_informations = jwt_handler.decode_jwt_token(token)
    
    assert token_informations["username"] == body["username"]
    assert token_informations["lalala"] == body["lalala"]

def test_revoke_jwt_token():
    jwt_handler = JwtHandler()

    body = {
        "username": "olaMundo",
        "aqui": "estou aqui",
        "lalala": ""
    }

    token = jwt_handler.create_jwt_token(body)
    is_revoked = jwt_handler.revoke_jwt_token(token)
    revoked_tokens = jwt_handler.get_revoke_list()
    
    assert isinstance(is_revoked, bool)
    assert revoked_tokens is not None
    
    with pytest.raises(Exception):
        jwt_handler.decode_jwt_token(token)

def test_clear_revoke_list():
    jwt_handler = JwtHandler()
    
    body = {
        "username": "olaMundo",
        "aqui": "estou aqui",
        "lalala": ""
    }
    
    token = jwt_handler.create_jwt_token(body)
    jwt_handler.revoke_jwt_token(token)
    jwt_handler.clear_revoke_list()
    revoked_tokens = jwt_handler.get_revoke_list()
    
    assert len(revoked_tokens) == 0
    assert revoked_tokens == set()
    
    token_informations = jwt_handler.decode_jwt_token(token)
    
    assert token_informations["username"] == body["username"]
    assert token_informations["lalala"] == body["lalala"]
    
def test_get_jwt_infos():
    jwt_handler = JwtHandler()
    
    jwt_infos = jwt_handler.get_jwt_infos()
    
    assert jwt_infos is not None
    assert jwt_infos["KEY"] is not None
    assert jwt_infos["ALGORITHM"] is not None
    assert jwt_infos["JWT_HOURS"] is not None
    assert jwt_infos["KEY"] == "shhhh"
    assert jwt_infos["ALGORITHM"] == "HS256"
    assert jwt_infos["JWT_HOURS"] == "24"