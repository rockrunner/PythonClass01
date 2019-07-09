import pymysql

class DataBase:
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', '123456', 'woniusale', charset='utf8')
        self.cursor = self.conn.cursor()

    def query_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def query_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def update_data(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        self.cursor.close()

if __name__ == '__main__':
    db = DataBase()

    db.update_data("update user set password='lm123' where userid=2")

    result = db.query_all('select * from user')
    print(result)