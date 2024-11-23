from flask import Flask, request, jsonify

# In-memory database
todos = []
current_id = 1

def options_todos():
    return '', 200  # Returns 200 OK for OPTIONS requests

def get_todos():
    return jsonify(todos), 200

def create_todo():
    global current_id
    data = request.get_json()
    data['id'] = current_id
    current_id += 1
    todos.append(data)
    return jsonify(data), 201

def get_todo_by_id(id):
    todo = next((item for item in todos if item['id'] == id), None)
    if todo:
        return jsonify(todo), 200
    return jsonify({'error': 'To-do item not found'}), 404

def update_todo_by_id(id):
    todo = next((item for item in todos if item['id'] == id), None)
    if todo:
        data = request.get_json()
        todo.update(data)
        return jsonify(todo), 200
    return jsonify({'error': 'To-do item not found'}), 404

def delete_todo_by_id(id):
    global todos
    todos = [item for item in todos if item['id'] != id]
    return '', 204
