from .clear_revoked_tokens import ClearRevokedTokens

def test_revoking_process():
    clear_revoked_tokens = ClearRevokedTokens()
    response = clear_revoked_tokens.clear_revoked_tokens()

    assert response["message"] == "Revoked tokens cleared"