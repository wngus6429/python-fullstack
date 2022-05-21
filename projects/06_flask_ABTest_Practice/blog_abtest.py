from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
import os

# from blog_view import blog

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# HTML파일에서 가져올 데이터는 static에서 가져와라
app = Flask(__name__, static_url_path='/static')
CORS(app) #여기서는 쓰지 않지만
app.secret_key = 'dave_server' #flask 로그인과 관련
# 랜덤으로 하면 자꾸 세션이 풀리니까

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')
login_manager = LoginManager()
login_manager.init_app(app) # 앱을 등록시켜줘야함
login_manager.session_protection = 'strong' #세션 복잡하게 만드는 정도


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
# 로그인 안된 사용자가 로그인이 된 사용자만 접근할수 있는 
# API들을 리퀘스트 했을경우에 에러가 나면서 이 함수가 호출됨
def unauthorized():
    return make_response(jsonify(success=False), 401)
# 401 허용 안 됨

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)