import psycopg2

from project.config.environment import DATABASE_URL


class PostgresConnector:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.connection = psycopg2.connect(**DATABASE_URL)

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection

    def __del__(self):
        self.connection.close()
