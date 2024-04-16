#!/usr/bin/python3

from sqlalchemy import *
from sqlalchemy.orm import *
from dotenv import load_dotenv
import os

load_dotenv()


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        try:
            self.__engine = sqlalchemy.create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    'hbnb_dev', 'hbnb_dev_pwd', 'hbnb_dev_db'),
                pool_pre_ping=True)
            Session = sessionmaker(bind=self.__engine)
            session = Session()
        except Exception:
            raise Exception("couldn't connect to server")
            return

        if os.environ['HBNB_ENV'] == 'test':
            for tbl in reversed(meta.sorted_tables):
                self.__engine.execute(tbl.delete())
