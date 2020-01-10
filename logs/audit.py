import datetime
import os
from threading import Thread
from unidecode import unidecode
import pytz

from design_patterns.singleton import Singleton


class Audit(metaclass=Singleton):

    def __init__(self):
        self.key = "INICIALIZACAO"
        self.project = "INICIALIZACAO"

    def set_info(self, key, project):
        if key and key != "":
            self.key = key
            self.project = project

    def insert_audit_log(self, message, threading=False):
        message = unidecode(message)
        if threading:
            Thread(target=self.__write_file, args=(message,)).start()
        else:
            self.__write_file(message)

    def __write_file(self, message):
        try:
            date_format = datetime.datetime.now(tz=pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')
            print(
                '[' + date_format + '] - [' + self.project + '] - '
                + self.key + ' - ' + message + '\n')
            if not os.path.isfile("crawler.log"):
                with open("crawler.log", "w") as f:
                    f.write('[' + date_format + '] - [' + self.project
                            + '] - ' + self.key + ' - ' + message + '\n')
            else:
                with open("crawler.log", "a") as f:
                    f.write('[' + date_format + '] - [' + self.project
                            + '] - ' + self.key + ' - ' + message + '\n')
        except Exception as exc:
            print('Error on print log: ' + str(exc))
