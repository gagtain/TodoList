from rest_framework import status
from rest_framework.exceptions import APIException


class CodeDataException(APIException):
    default_code = 'invalid'

    def __init__(self, detail: str | dict, code: int = status.HTTP_400_BAD_REQUEST):
        self.status_code = code
        super().__init__(detail, code)
