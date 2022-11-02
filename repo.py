from mysql.connector import connect, Error


class Repo:
    ROLE_INSPECTOR = 1
    ROLE_CLEANER = 2
    ROLE_SUPERVISOR = 3

    def __init__(self, host, user, password, db):
        self.connection = None
        self.cursor = None
        self.connect_to_db(host, user, password, db)
        if self.connection is not None and self.cursor is not None:
            self.select_db(db)

            self.get_user = lambda u: self.raw_query(f"SELECT * FROM user WHERE username='{u}'")
            self.get_user_by_id = lambda id: self.get_query(f"SELECT * FROM user u JOIN role r ON u.role_id=r.id, u.id='{id}'")
            self.login_user = lambda u, p: self.get_query(f"SELECT * FROM user WHERE username='{u}' AND password='{p}'")
            self.add_user = lambda u, p, f, r: self.write_query(f"INSERT INTO user SET username='{u}', password='{p}', fio='{f}', role_id='{r}'")
            self.get_users = lambda: self.raw_query("SELECT * FROM user JOIN role ON user.role_id=role.id")
            self.get_roles = lambda: self.raw_query("SELECT * FROM role")
            self.rm_user = lambda id: self.write_query(f"DELETE FROM user WHERE id='{id}'")

            self.get_clients = lambda: self.raw_query("SELECT * FROM client WHERE hidden='0'")
            self.add_client = lambda f, n, a: self.write_query(f"INSERT INTO client SET fio='{f}', number='{n}', address='{a}'")
            self.rm_client = lambda id: self.write_query(f"UPDATE client SET hidden='1' WHERE id='{id}'")

            self.get_orders = lambda: self.raw_query("SELECT * FROM cleaning.order o JOIN client c, clothing_type t, cleaning_type cl, status s WHERE o.client_id=c.id AND o.clothing_type_id=t.id AND o.cleaning_type_id=cl.id AND o.status_id=s.id ORDER BY date ASC")
            self.add_order = lambda c, t, n, cl: self.write_query(f"INSERT INTO cleaning.order SET `client_id`='{c}', `clothing_type_id`='{t}', `name`='{n}', `cleaning_type_id`='{cl}'")
            self.rm_order = lambda id: self.write_query(f"DELETE FROM cleaning.order WHERE id='{id}'")
            self.change_order_status = lambda id, s: self.write_query(f"UPDATE cleaning.order SET status_id='{s}' WHERE id='{id}'")
            self.get_stats = lambda: self.raw_query("SELECT DATE_FORMAT(date, '%d-%m-%Y'), COUNT(*), SUM(price) FROM cleaning.order JOIN cleaning_type c ON cleaning_type_id=c.id GROUP BY DATE_FORMAT(date, '%d-%m-%Y')")

            self.get_types = lambda: self.raw_query("SELECT * FROM clothing_type WHERE hidden=0")
            self.add_type = lambda n: self.write_query(f"INSERT INTO clothing_type SET name='{n}'")
            self.rm_type = lambda id: self.write_query(f"UPDATE clothing_type SET hidden=1 WHERE id='{id}'")

            self.get_cleanings = lambda: self.raw_query("SELECT * FROM cleaning_type WHERE hidden=0")
            self.add_cleaning = lambda n, p: self.write_query(f"INSERT INTO cleaning_type SET name='{n}', price='{p}'")
            self.rm_cleaning = lambda id: self.write_query(f"UPDATE cleaning_type SET hidden=1 WHERE id='{id}'")

            self.get_statuses = lambda: self.raw_query("SELECT * FROM status")
            self.get_status_by_id = lambda id: self.get_query(f"SELECT name FROM status WHERE id={id}")
        else:
            print('connection failed')

    def connect_to_db(self, host, user, password, db):
        try:
            self.connection = connect(host=host, user=user, password=password)
            self.cursor = self.connection.cursor()
            self.cursor.execute("SHOW DATABASES")
            for res in self.cursor:
                if res[0] == db:
                    self.cursor.fetchall()
                    return
            for line in open('dump.sql'):
                self.cursor.execute(line)
            self.connection.commit()
            print('dump loaded successfully')
        except Error as e:
            print(e)

    def select_db(self, db):
        self.cursor.execute(f"USE {db}")

    def raw_query(self, query):
        if self.cursor and query:
            self.cursor.execute(query)
            return self.cursor.fetchall()

    def write_query(self, query):
        if self.cursor and query:
            self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()

    def get_query(self, query):
        if self.cursor and query:
            self.cursor.execute(query)
            return self.cursor.fetchone()

    def reg_user(self, u, p, f, r):
        if not self.get_user(u):
            self.add_user(u, p, f, r)
            return True
        else:
            return False
