import psycopg2
class User:
    def __init__(self, user_id, first_name, last_name, username):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def chekIndatabase(self):
        conn = psycopg2.connect(database="Db", user="postgres", password="12345", host="localhost", port=5432)
        cur = conn.cursor()
        cur.execute("INSERT INTO telegram.chat (user_id, first_name,last_name,username) VALUES (%s, %s, %s, %s)", (self.user_id, self.first_name, self.last_name, self.username))
        conn.commit()
        return conn

    def testUser(self):
        return self.user_id

    def checkUser(self):
        return self.first_name
