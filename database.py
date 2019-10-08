import os

from sqlalchemy import create_engine


class DBase:
    def __init__(self):
        engStr = 'postgres+psycopg2://' + os.environ['DBUser'] + ':' +  \
            os.environ['DBPass'] + '@' + \
            os.environ['DBHost'] + ':5432/' + os.environ['DBDatabase']

        self.engine = create_engine(engStr)
