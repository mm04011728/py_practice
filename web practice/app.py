#coding:utf-8

from flask import  Flask, request, render_template,redirect, url_for
import db

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
    success,name = db.authenticate(loginid,password)
    # print(success,name)
    if success:
        return redirect(url_for('book',user_name=name))
        # return render_template('index.html', username=name)
    return render_template('login.html', message='用户名或密码错误', loginid=loginid)
    
@app.route('/book/<user_name>',methods = ['GET'])
def book(user_name):
    books = db.get_all_books()
    return render_template('index.html',user_name= user_name,books = books)

if __name__ == '__main__':
    # print(db.get_all_books())
    app.run()