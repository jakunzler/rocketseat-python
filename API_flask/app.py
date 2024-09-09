from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD configuration
# Create, Read, Update, Delete
# Tabela: Tarefa

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(
        id=len(tasks) + 1,
        title=data['title'],
        description=data.get("description", "")
    )
    tasks.append(task)
    return jsonify({'message': 'Task created successfully'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', method=['PUT'])
def update_task(id):
    task = None
    data = request.get_json()
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "Task not found"}), 404

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.completed = data.get("completed", task.completed)
    
    return jsonify({"message": "Task updated successfully"})

if __name__ == "__main__":
    app.run(debug=True)