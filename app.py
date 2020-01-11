from flask import Flask
from flask_restful import Api, Resource

from connections.db_controller import DbController
from logs.audit import Audit
from settings import X_API_KEY
from utils.crypt import Crypt

app = Flask(__name__)
api = Api(app)


class Notes(Resource):
    def __init__(self):
        self.db = DbController()
        self.crypt = Crypt()
        self.audit = Audit()
        self.audit.set_info(X_API_KEY, 'Arquivei-Consulta')

    def get(self, note):
        notes = self.db.select_all_keys()
        for dbnote in notes:
            if note == self.crypt.decrypt(dbnote[1]):
                self.audit.insert_audit_log('Nota pesquisada: {} - Encontrada'.format(note))
                return self.crypt.decrypt(dbnote[2]), 200
        self.audit.insert_audit_log('Nota pesquisada: {} - Nao encontrada'.format(note))
        return "Nota nao encontrada", 404


api.add_resource(Notes, "/notes/<string:note>")
app.run(debug=True)

