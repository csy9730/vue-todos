from flask import request
from flask import Flask, render_template, jsonify
from random import *
import random
from flask_cors import CORS
import requests

# app = Flask(__name__,
#             template_folder="../../frontend/dist",
#             static_folder="../../frontend/dist/static")

app = Flask(__name__,
            static_folder = "./todo/static",
            template_folder = "./todo")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


class TodoList:
    def __init__(self) -> None:
        self.data = []

    def add(self, todo=None):
        if not todo:
            N = random.randint(1,6)
            todo = {
                "id": random.randint(100, 1000),
                "title": randomText(),# 随机标题
                "isDelete": False, #  是否删除
                "locked": False, # 随机锁定
                "record": [{"text": randomText(),"isDelete": False, "checked": False} for i in range(N)]
            }
        self.data.append(todo)

    def find(self, tid:int):
        todo = {}
        for i,td in enumerate(self.data):
            if str(td["id"]) == str(tid):
                todo = td
                break
        return todo, i

    def __getitem__(self, idx):
        return self.data[idx]
    
    def __setitem__(self, idx, v):
        self.data[idx] = v

    def __len__(self):
        return len(self.data)
    
    

Todos = TodoList()


def randomText(N=8):
    bs = "abcdefghijklmnopqrstuvwxyz"
    rr = []
    for i in range(N):
        r = random.randint(0, 25)
        rr.append(bs[r])
    return ''.join(rr)
    
for i in range(5) : 
    Todos.add()

# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# 生成词云图片接口，以base64格式返回
# @app.route('/word/cloud/generate', methods=["POST"])
# def cloud():
#     text = request.json.get("word")
#     return ""


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     if app.debug:
#         return requests.get('http://localhost:8080/{}'.format(path)).text
#     return render_template("index.html")


@app.route('/todo/list')
def todo_list():
    response = {
        'todos': Todos.data
    }
    return jsonify(response)

@app.route('/todo/listId')
def todo_id():
    tid = request.args.get('id')
    print(tid)
    todo, idx = Todos.find(tid)
    print(Todos[idx])
    response = {
        "todo": todo
    }
    return jsonify(response)

@app.route('/todo/addTodo', methods=["POST"])
def todo_add():
    id = randint(111, 3000)
    todo = {
        "id": id,
        "title": 'newList',
        "isDelete": False,
        "locked": False,
        "record": []
    }
    Todos.add(todo)
    return jsonify(todo)

@app.route('/todo/editTodo', methods=["POST"])
def todo_edit_id():
    td = request.get_json()['todo']
    print(td)
    tid = td["id"]
    todo, idx = Todos.find(tid)
    todo.update(td)
    # print(todo)
    Todos[idx] = todo
    return jsonify({
        "err": 200
    })

@app.route('/todo/addRecord', methods=["POST"])
def todo_addRecord():
    td = request.get_json()
    print(td)
    todo, _ = Todos.find(td["id"])
    stodo = {
        "text": td["text"],
        "isDelete": False,
        "checked": False,
    }
    todo["record"].append(stodo)
    return jsonify({
        "err": 200
    })

@app.route('/todo/editRecord', methods=["POST"])
def todo_editRecord():
    td = request.get_json()
    print(td)
    index = td["index"]
    todo, idx = Todos.find(td["id"])
    todo["record"][index] = td["record"]
    Todos[idx] = todo
    return jsonify({
        "err": 200
    })
