import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='dave',
    passwd='funcoding',
    db='blog_db',
    charset='utf8'
)

def conn_mysqldb():
    # pymysql에서 .open 이라는 기능으로 연결되어 있는지 확인
    if not MYSQL_CONN.open:
        # 연결 안되어 있으니 재접속 하는 구문
        MYSQL_CONN.ping(reconnect=True)
    # 연결 잘 되어 있으면 그냥 리턴만 해주면 되는거지
    return MYSQL_CONN