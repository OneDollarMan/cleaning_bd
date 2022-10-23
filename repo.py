from mysql.connector import connect, Error


class Repo:

    def __init__(self, host, user, password, db):
        self.connection = None
        self.cursor = None
        self.connect_to_db(host, user, password, db)
        if self.connection is not None and self.cursor is not None:
            ...
        else:
            print('connection failed')

    def connect_to_db(self, host, user, password, db):
        try:
            connection = connect(host=host, user=user, password=password)
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            for res in cursor:
                if res[0] == db:
                    self.connection = connection
                    self.cursor = cursor
                    return
            for line in open('dump.sql'):
                cursor.execute(line)
            connection.commit()
            print('dump loaded successfully')
            self.connection = connection
            self.cursor = cursor
        except Error as e:
            print(e)
