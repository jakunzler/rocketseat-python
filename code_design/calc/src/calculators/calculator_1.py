from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        print(input_data)
        
    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Invalid body format")
          
        input_data = body["number"]
        return input_data