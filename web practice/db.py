# coding:utf-8

import sqlite3
import hashlib,random
import os

# abs_path = os.path.abspath('.')
# print(abs_path)
DBPATH = ".\\db\\web.db"
# print(DBPATH)

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def get_salt():
    return ''.join([chr(random.randint(48, 122)) for i in range(8)])

def get_user_list():
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("select * from sys_user")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def authenticate(loginID, password):
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute(
        r"select loginID,name,password,salt from sys_user where loginID='{0}'".format(loginID))
    users = cursor.fetchall()
    print(users)
    cursor.close()
    conn.close()
    for id, name, pw, salt in users:
        # print(id, name, pw, salt)
        if loginID == id and pw == get_md5(password+salt):
            return True, name
    return False,None

def get_all_books():
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute(
        'select ISBN,name,author,publishing,introduction from book')
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books

def get_book(ISBN):
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute(
        'select ISBN,name,author,publishing,introduction from book where SN=?', (ISBN,))
    book = cursor.fetchall()
    cursor.close()
    conn.close()
    return book[0]

def new_user(loginID,password,name):
    salt = get_salt()
    pw = get_md5(password+salt)
    sql_query = r"insert into sys_user values ('{0}','{1}','{2}','{3}')".format(loginID,name,pw,salt)
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    return row ==1

def main():
    # books = get_all_books()
    # for book in books:
    #     print(book)
    # success = new_user("admin","admin","管理员")
    # success = new_user("guest","guest","访客")
    # print(success)
    # authenticate("admin","admin")
    users = get_user_list()
    print(users)
    pass
if __name__ == '__main__':
    main()