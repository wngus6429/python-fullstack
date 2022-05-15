from flask import Flask
import requests

app = Flask(__name__)

#app.debug가 true면 로깅하지 말라
#true면 개발자가 테스트중이니까.
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler  # logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler('dave_server.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)  # 어느 단계까지 로깅을 할지를 적어줌
    # app.logger.addHandler() 에 등록시켜줘야 app.logger 로 사용 가능
    app.logger.addHandler(file_handler)


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('이것은 중요한 에러입니다. page_not_found에서 일어났습니다.')
    return "<h1>우이씨 해당 경로에 맞는 웹페이지가 없습니다. 문제가 지속되면, 죄송하지만 관리자에게 연락해주세요</h1>", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=False)
    # 뒤에 debug가 true면 나오는 양이 많아져서 디버깅 하기 좋겟지