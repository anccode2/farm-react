import requests


def test_get_tasks():
    response = requests.get("http://localhost:8000/api/tasks")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verificar que se obtengan tareas


def test_get_task():
    response = requests.get(
        "http://localhost:8000/api/tasks/64a423dc1272f4e3be72efd2")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verificar que se obtengan tareas


def test_create_task():
    task_data = {
        "title": "Nueva tareaaaaaa",
        "description": "Descripción de la nueva tarea",
    }
    response = requests.post("http://localhost:8000/api/tasks", json=task_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Nueva tareaaaaaa"
    assert response.json()["description"] == "Descripción de la nueva tarea"


def test_put_task():
    updated_task_data = {
        "title": "Tarea actualizada",
        "description": "Descripción actualizada",
        "completed": "false",
    }
    response = requests.put(
        "http://localhost:8000/api/tasks/64a423dc1272f4e3be72efd2",
        json=updated_task_data,
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Tarea actualizada"
    assert response.json()["description"] == "Descripción actualizada"


def test_delete_task():
    response = requests.delete(
        "http://localhost:8000/api/tasks/64a476481220929eda0d4f05")
    assert response.status_code == 200
    assert response.text.strip('"') == "successfully removed task"
