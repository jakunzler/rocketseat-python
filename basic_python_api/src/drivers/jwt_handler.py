from datetime import datetime, timedelta, timezone
from typing import Dict
import jwt
from src.configs.jwt_configs import jwt_infos

invalid_tokens = set()

class JwtHandler:
    def create_jwt_token(self, body: Dict = {}) -> str: # pylint: disable=missing-function-docstring dangerous-default-value
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=int(jwt_infos["JWT_HOURS"])),
                **body,
            },
            key=jwt_infos["KEY"],
            algorithm=jwt_infos["ALGORITHM"]
        )
        return token
    
    def decode_jwt_token(self, token: str) -> Dict: # pylint: disable=missing-function-docstring
        if token in invalid_tokens:
            raise jwt.InvalidTokenError("Token has been revoked")
        token_information =jwt.decode (
            token,
            key=jwt_infos["KEY"],
            algorithms=jwt_infos["ALGORITHM"]
        )
        return token_information
    
    def revoke_jwt_token(self, token: str): # pylint: disable=missing-function-docstring
        invalid_tokens.add(token)
        return True
    
    def get_revoked_list(self):
        return invalid_tokens
    
    def clear_revoked_list(self):
        invalid_tokens.clear()
        return True

    def get_jwt_infos(self):
        return jwt_infos
    