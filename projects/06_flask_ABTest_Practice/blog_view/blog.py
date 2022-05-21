from flask import Flask, Blueprint, request, render_template

blog_abtest = Blueprint('blog', __name__)

# 여기 주소 이름과 아래 함수 이름 같게 해야함
@blog_abtest.route('/test')
def test():
    return render_template('blog_A.html')

@blog_abtest.route('/wngus')
def wngus():
    return render_template('blog_B.html')
