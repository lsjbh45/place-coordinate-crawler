import psycopg2


class Database:
    def __init__(self, host, port, user, password, database):
        self.db = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def fetchall(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def commit(self):
        self.db.commit()
