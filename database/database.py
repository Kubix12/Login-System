import psycopg2


class Database:
    def __init__(self, database_name, database_user, database_password, database_host, database_port):
        self.database_name = database_name
        self.database_user = database_user
        self.database_password = database_password
        self.database_host = database_host
        self.database_port = database_port

    def create_table(self):
        """create_table function creates table if no other exists with the same name
        :return:
        """
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users(ID SERIAL PRIMARY KEY, LOGIN TEXT, PASSWORD TEXT);")
        print('Table created')
        conn.commit()
        conn.close()

    def insert_data(self, login, user_password):
        """insert_data function inserts data into existing table
        :param login: describe
        :param user_password: describe
        """
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f'INSERT INTO users{login, user_password} VALUES (%s, %s);'
        cur.execute(query, (login, user_password))
        print("Data inserted successfully")
        conn.commit()
        conn.close()

    def search_data(self, login, user_password):
        """search_data function checks that login and password already exists in table
        :param login:
        :param user_password:
        :return: True if login and password exists in table and user can log in into application
        False if login and password doesn't exist in table and user can only register and then log in
        """
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f'SELECT COUNT(*) FROM users WHERE LOGIN = %s and PASSWORD = %s'
        cur.execute(query, (login, user_password))
        result = cur.fetchone()
        count = result[0]
        conn.close()
        if count > 0:
            return True
        else:
            self.insert_data(login, user_password)
            return False


# Database setting
name = 'demo'
user = 'postgres'
password = '123'
host = 'localhost'
port = '5432'

db = Database(name, user, password, host, port)
db.create_table()
