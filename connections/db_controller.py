import unicodedata
from datetime import datetime
from multiprocessing import Process, Manager

import pymysql

from design_patterns.singleton import Singleton
from settings import DB_NAME, DB_TABLE_NOTES
from logs.audit import Audit


class DbController(metaclass=Singleton):

    def __init__(self, db_name=None):
        self.db_name = db_name if db_name else DB_NAME
        self.conn = self.connect()
        self.audit = Audit()

    def connect(self):
        host = 'localhost'
        port = 3306
        user = 'root'
        password = 'root'

        return pymysql.connect(
                   host=host,
                   port=port,
                   user=user,
                   password=password,
                   db=self.db_name,
                   charset='utf8mb4'
                )

    def insert(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            id = cursor.lastrowid
            cursor.close()
            return id
        except Exception as e:
            raise Exception('error saving on table: ' + str(e))

    def select(self, sql, dict=False):
        try:
            if dict:
                cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            else:
                cursor = self.conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except pymysql.Error as e:
            self.audit.insert_audit_log('error select on table: ' + str(e))


    def insert_file(self, access_key, value, table=DB_TABLE_NOTES):
        try:
            sql = """INSERT INTO {} (access_key, value) VALUES ('{}','{}')""".format(table, access_key, value)
            return self.insert(sql)
        except Exception as e:
            self.audit.insert_audit_log('Error insert new file: ' + str(e))

    def select_all_keys(self, table=DB_TABLE_NOTES):
        try:
            sql = """SELECT * FROM {}""".format(table, dict=True)
            return self.select(sql)
        except Exception as e:
            self.audit.insert_audit_log('Error insert new file: ' + str(e))
