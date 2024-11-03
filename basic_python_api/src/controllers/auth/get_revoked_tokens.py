from flask import request
from typing import Dict
from src.drivers.jwt_handler import JwtHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError
from ..interfaces.auth.get_revoked_tokens import GetRevokedTokensInterface

from src.drivers.jwt_handler import invalid_tokens

class GetRevokedTokens(GetRevokedTokensInterface):
    def __init__(self) -> None:
        self.__jwt_handler = JwtHandler()