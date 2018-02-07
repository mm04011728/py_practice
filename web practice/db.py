# coding:utf-8

import sqlite3
import hashlib,random

DBPATH = "db\\web.db"


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def get_salt(parameter_list):
    return ''.join([chr(random.randint(48, 122)) for i in range(8)])


def authenticate(loginID, password):
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute(
        'select loginID,name,password,salt from sys_user where loginID=?', (loginID,))
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    for id, name, pw, salt in users:
        if loginID == id and pw == get_md5(password+salt):
            return True, name
    return False

def get_all_books():
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute(
        'select SN,name,author,publishing from book')
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books

def get_book(SN):
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute(
        'select SN,name,author,publishing from book where SN=?', (SN,))
    book = cursor.fetchall()
    cursor.close()
    conn.close()
    return book[0]