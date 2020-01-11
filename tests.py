import json
import unittest

from connections.db_controller import DbController
from logs.audit import Audit
from utils.consult import Consult
from utils.crypt import Crypt


class TestClasses(unittest.TestCase):

    def test_response_validation(self):
        obj = Consult()
        response = {'status': {'code': 200}}
        self.assertEqual(obj.response_validation(response), True)

    def test_api_response(self):
        obj = Consult()
        self.assertEqual(self.validate_json(obj.get_information()), True)

    @staticmethod
    def validate_json(test):
        if isinstance(test, dict):
            return True
        return False

    def test_audit_singleton(self):
        obj1 = Audit()
        obj1.set_info('a', 'b')
        obj2 = Audit()
        self.assertEqual(obj2.key, 'a')
        self.assertEqual(obj2.project, 'b')

    def test_db_connection(self):
        obj = DbController()
        self.assertEqual(obj.conn.open, True)

    def test_crypto(self):
        obj = Crypt()
        text = obj.encrypt('teste crypto')
        self.assertEqual(obj.decrypt(text), 'teste crypto')


if __name__ == '__main__':
    unittest.main()
