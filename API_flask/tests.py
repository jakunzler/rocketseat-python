import pytest
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000/'
tasks = []

def test_create_task():
    new_task_data = {'title': 'Task 1', 'description': 'Description 1'}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    assert response.json()['message'] == 'Task created successfully'
    assert "id" in response.json()
    tasks.append(response.json())
    
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert len(response.json()['tasks']) == len(tasks)
    assert "tasks" in response.json()
    assert "total_tasks" in response.json()
    
def test_get_task():
    if tasks:
        task = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task['id']}")
        assert response.status_code == 200
        assert response.json()['id'] == task['id']
        
def test_update_task():
    if tasks:
        task = tasks[0]
        payload = {'completed': True, 'title': 'Task 1 updated', 'description': 'Description 1 updated'}
        response = requests.put(f"{BASE_URL}/tasks/{task['id']}", json=payload)
        assert response.status_code == 200
        assert response.json()['message'] == 'Task updated successfully'
        
        # Nova requisição para verificar se os dados foram atualizados
        response = requests.get(f"{BASE_URL}/tasks/{task['id']}")
        assert response.status_code == 200
        assert response.json()['id'] == task['id']
        assert response.json()['title'] == payload['title']
        assert response.json()['description'] == payload['description']
        assert response.json()['completed'] == payload['completed']
        
def test_delete_task():
    if tasks:
        task = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task['id']}")
        assert response.status_code == 200
        assert response.json()['message'] == 'Task deleted successfully'
        
        # Nova requisição para verificar se a tarefa foi deletada
        response = requests.get(f"{BASE_URL}/tasks/{task['id']}")
        assert response.status_code == 404
        assert response.json()['message'] == 'Task not found'