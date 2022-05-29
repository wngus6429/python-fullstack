from flask_login import UserMixin
from db_model.mysql import conn_mysqldb
#* db_model폴더의 mysql 파일안에 conn_mysqldb 함수 사용
#! 여기는 MySQL 접속 예정 # 사용자 관리

class User(UserMixin):

    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id # flask_login에서도 쓰기 떄문에 이름 바꾸면 에러
        self.user_email = user_email
        self.blog_id = blog_id

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + str(user_id) + "'"
        # print (sql) 위에 보면 "" ' 이런거 때문에 헷갈림 그래서 찍어보는거임
        # 확인 해보고 코드에 작동시켜 보는게 좋지
        db_cursor.execute(sql)
        user = db_cursor.fetchone() # 매칭되는 코드 하나만 하면 되니까
        if not user:
            return None
        
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        return user


    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" + str(user_email) + "'"
        # print (sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        return user


    @staticmethod
    def create(user_email, blog_id):
        user = User.find(user_email) # 위에 find메소드
        if user == None: # 위에 41번
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user
    
    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted #이거 딱히 안 적어도 ㅋㅋ, 0을 돌려주면 없다는거지
        # 혹시나 조건식으로 뭔가 할때를 대비해서 return을 한것이다.