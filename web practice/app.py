#coding:utf-8

from flask import  Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('login.html')

# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
    loginid = request.form['loginid']
    password = request.form['password']
    if loginid=='admin' and password=='password':
        return render_template('index.html', username=loginid)
    return render_template('login.html', message='用户名或密码错误', username=loginid)

if __name__ == '__main__':
    app.run()