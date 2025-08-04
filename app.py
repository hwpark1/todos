from flask import Flask, request, jsonify, Response
import os
import json

app = Flask(__name__)

DATA_FILE = 'todos.json'

def load_todos():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []

def save_todos(todos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def get_next_id(todos):
    return max((todo['id'] for todo in todos), default=0) + 1

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = load_todos()
    return jsonify({'todos': todos})

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'task' not in data or not data['task'].strip():
        return jsonify({'error': 'task 필드는 필수입니다'}), 400

    todos = load_todos()
    new_todo = {
        'id': get_next_id(todos),
        'task': data['task'],
        'completed': False
    }
    todos.append(new_todo)
    save_todos(todos)
    return jsonify({'message': '할일이 추가되었습니다', 'id': new_todo['id']}), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            save_todos(todos)
            return jsonify({'message': '할일 상태가 변경되었습니다'})
    return jsonify({'error': '해당 할일을 찾을 수 없습니다'}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos = load_todos()
    filtered_todos = [todo for todo in todos if todo['id'] != todo_id]
    if len(filtered_todos) == len(todos):
        return jsonify({'error': '해당 할일을 찾을 수 없습니다'}), 404
    save_todos(filtered_todos)
    return jsonify({'message': '할일이 삭제되었습니다'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

