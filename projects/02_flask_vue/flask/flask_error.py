from flask import Flask
import requests

app = Flask(__name__)

#! 없는 페이지를 요청했을 때의 에러
#플래스크에서 에러를 핸들링하는 기능도 가지고 있다.
@app.errorhandler(404)
def page_not_found(error):
    #뒤에 404를 보내면서 직접 에러코드를 보낼수도 있다.
    return "<h1>404 Error에러떳당</h1>", 404


@app.route("/naver")
def get_google():
    response = requests.get("http://www.naver.com")
    return response.text

@app.route("/google")
def get_my():
    return "<h2>내맘대로 한다</h2>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
