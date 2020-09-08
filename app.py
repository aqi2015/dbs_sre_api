"""
@File    : app.py
@Time    : 2020/7/17 2:30 下午
@Author  : Akiqi
@Email   : linqi03@beyondsoft.com
@Software: PyCharm
"""
from flask import Flask, request
from flask_restful import Api, Resource
from services import api as sre

app = Flask(__name__)
api = Api(app)
api.add_resource(sre.Task, '/task/', '/task/<worker>')

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True)
