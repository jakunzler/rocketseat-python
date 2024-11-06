import uuid
from .get_revoked_tokens import GetRevokedTokens

mock_token = str(uuid.uuid4())

def test_getting_revoked_tokens():
    

    get_tokens_object = GetRevokedTokens()
    revoked_tokens = get_tokens_object.get_revoked_tokens()
    
    assert revoked_tokens == {
        "revoked_tokens": set()
    }