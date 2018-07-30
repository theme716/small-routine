import pymysql

class Mysql():
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','123456','reptile',charset='utf8')
        self.cursor = self.conn.cursor()
    def execute(self,sql,data):
        try:
            row = self.cursor.execute(sql,data) #返回影响行数
            self.conn.commit()
            print(data)
        except Exception as e:
            print(e)
            self.conn.rollback()
    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    mysql = Mysql()
