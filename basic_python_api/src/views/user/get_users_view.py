from src.controllers.interfaces.user.get_users import GetUsersInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from ..interfaces.view_interface import ViewInterface

class GetUsersView(ViewInterface):
    def __init__(self, controller: GetUsersInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        page_length = None
        if body and "page_length" in body:
            page_length = body.get("page_length")
        
        if page_length is None:
            response = self.__controller.get_users()
            return HttpResponse(body={ "data": response }, status_code=200)
          
        response = self.__controller.get_users(page_length)
            
        return HttpResponse(body={ "data": response }, status_code=200)
      
      

