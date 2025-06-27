class HttpResponse:
    def __init__(self, body: dict, status_code: int) -> None:
        self.body = body
        self.status = status_code
