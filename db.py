import psycopg2

class Database:
    def __init__(self, dbname, user, password, host="localhost",port=5432):
        self.dbname = dbname
        self.user = user
        self.password =  password
        self.host = host
        self.port = port
        self.conn = psycopg2.connect(dbname=self.dbname, 
                                     user=self.user, 
                                     password=self.password, 
                                     host=self.host, 
                                     port=self.port
                                     )
        self.cur = self.conn.cursor()
    def sql_excute(self, sql_query, data=None):
        try:
            if data:
                self.cur.execute(sql_query, data)
            else:
                self.cur.execute(sql_query)
        except Exception as error:
            print(error)
        self.conn.commit()
    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        age INT,
        adress VARCHAR(255),
        phone VARCHAR(50)
        )"""
        self.sql_excute(sql)
        self.conn.commit()
    def add_users(self, tp: tuple):
        try:
            sql = """INSERT INTO users (id, first_name, last_name, age, adress, phone) VALUES (%s, %s, %s, %s, %s, %s)"""
            self.sql_excute(sql, tp)
            self.conn.commit()
            return True
        except Exception as error:
            print(error)
            return False