import base64

import requests

from logs.audit import Audit
from settings import URL_API, X_API_KEY, X_API_ID


class Consult(object):

    def __init__(self, x_api_key=X_API_KEY):
        self._url_api = URL_API
        self._x_api_id = X_API_ID
        self._x_api_key = x_api_key
        self.audit = Audit()

    def get_information(self):
        try:
            headers = {"Content-Type": "application/json", "x-api-id": self._x_api_id, "x-api-key": self._x_api_key}
            response = requests.get(self._url_api, headers=headers).json()
            if self.response_validation(response):
                return response
            else:
                self.audit.insert_audit_log('Consulta retornou resposta inesperada: {} - {}'.
                                            format(response['status']['code'], response['status']['message']))
                return None
        except Exception as e:
            self.audit.insert_audit_log('Erro: {}'.format(e))

    @staticmethod
    def response_validation(response):
        if response['status']['code'] == 200:
            return True
        else:
            return False

