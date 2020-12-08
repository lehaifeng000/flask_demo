import pymysql


class MyDB():
    def __init__(self):
        self.conn = pymysql.connect("10.11.47.114", "lhf", "lhf123", "sjk_demo")
        # 返回值为dict形式
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def get_conn(self):
        pass

    def get_user(self, user_name):
        self.cursor.execute("select id,name,password,level from user where name=%s", (user_name,))
        row = self.cursor.fetchone()
        return row

    def get_stus(self):
        self.cursor.execute("select id,name from user where level=1")
        rows = self.cursor.fetchall()
        return rows

    def get_news(self):
        self.cursor.execute("select id,title,content,create_time from news")
        rows = self.cursor.fetchall()
        return rows

    def get_courses(self):
        self.cursor.execute("select id,name,teacher,score from course")
        rows = self.cursor.fetchall()
        return rows

    def add_user(self, name, password, level):
        self.cursor.execute("insert into user(name,password,level) values(%s,%s,%s)", (name, password, level))
        self.conn.commit()


db = MyDB()
# row=db.get_user('lhf')
# print(row)
