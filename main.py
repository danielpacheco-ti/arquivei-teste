import base64

from connections.db_controller import DbController
from logs.audit import Audit
from settings import X_API_KEY
from utils.consult import Consult
from utils.crypt import Crypt


class Main:

    def __init__(self):
        self.audit = Audit()
        self.audit.set_info(X_API_KEY, 'Arquivei-Consulta')
        self.db = DbController()
        self.api_consult = Consult()
        self.crypt = Crypt()

    def execute_consult(self):
        self.audit.insert_audit_log('Realizando consulta no endpoint do Arquivei')
        notes = self.api_consult.get_information()
        if notes:
            self.audit.insert_audit_log('{} notas encontradas'.format(len(notes['data'])))
            self.db_insert(notes)
        else:
            self.audit.insert_audit_log('Erro na consulta')

    def db_insert(self, notes):
        for note in notes['data']:
            self.audit.insert_audit_log('Inserindo chave de acesso: {}'.format(note['access_key']))
            access_key = self.crypt.encrypt(note['access_key'])
            value = self.crypt.encrypt(str(base64.b64decode(note['xml'])))
            self.db.insert_file(access_key, value)


if __name__ == '__main__':
    Main().execute_consult()

