from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# 이와 같이 선언해주면 전 요청/응답 헤더에 CORS 지원 헤더 정보를 넣어서, CORS를 지원해줌


@app.route("/test", methods=['GET'])
def test():
    return make_response(jsonify(success=True), 200) 
    #뒤에 status코드까지 넣어주기 위해 make_response 기능 사용
    #return jsonify(success=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
