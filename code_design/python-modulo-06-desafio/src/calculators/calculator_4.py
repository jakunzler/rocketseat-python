from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def calculate_average(self, numbers: list) -> dict:
        if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
            raise HttpUnprocessableEntityError("Lista de números não fornecida ou mal formatada!")

        average = sum(numbers) / len(numbers)
        response = self.__format_response(average)

        return response

    def __format_response(self, average: float) -> dict:
        return {
            "data": {
                "Calculator": 4,
                "average": round(average, 2)
            }
        }
