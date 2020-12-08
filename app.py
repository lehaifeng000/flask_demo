from flask import Flask, request
import json
from dao.db import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("hello")
    return 'Hello World!'


@app.route('/user/login/', methods=["POST", ])
def user_login():
    params = request.json
    print(params,type(params))
    user_name = params["user_name"]
    password = params["password"]
    row = db.get_user(user_name)
    res=dict()
    if row == None or len(row) == 0 or row['password'] != password:
        print("用户名或密码错误", user_name, password)
        res["code"]=1
        res["msg"]="用户名或密码错误"
        return json.dumps(res)
    else:
        print("登录成功")
        res["code"]=0
        res["msg"]="登录成功"
        return json.dumps(res)

    # user_name = request.form['name']
    # print(request.form)
    # print(request.data)
    # print(request.method)
    # print(request.values)
    # print(request.headers)
    # print(request.args)
    print(request.json)
    # print(json.load())
    return "yes"


if __name__ == '__main__':
    app.run()
