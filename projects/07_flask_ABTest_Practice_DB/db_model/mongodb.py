import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

def conn_mongodb():
    try:
        # 여기서 지금 연결되어 있는지 확인하고 안되어 있으면
        # except 구문으로 가서 mongoDB를 다시 실행시키는거지
        MONGO_CONN.admin.command('ismaster')
        # 문제 없을경우 밑에 코드가 실행되는거고
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab