from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from flask_login import current_user, login_user, logout_user
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
import datetime

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))
    else:
        # print('set_email', request.headers)
        # content type 이 application/json 인 경우
        # print('set_email', request.get_json())
        print('set_email', request.form['user_email'])
        print('블로그아이디', request.form['blog_id'])
        user = User.create(request.form['user_email'], request.form['blog_id']) 
        # session_mgmt.py 6번줄에 A
        # https://docs.python.org/3/library/datetime.html#timedelta-objects
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        
        return redirect(url_for('blog.fullstack'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)

@blog_abtest.route('/logout')
def logout():
    print('current_user', current_user)
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.fullstack'))

@blog_abtest.route('/fullstack')
def fullstack():
    # BlogSession.get_blog_page()
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(session['client_id'], current_user.user_email, webpage_name) #어노니머스는 아무거나
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        # 한번도 등록된적이 없는 사용자
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'], 'annonymous', webpage_name) #어노니머스는 아무거나
        return render_template(webpage_name) # blog_A파일의 65번쨰부터 실행