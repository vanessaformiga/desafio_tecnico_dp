import sys
import os
import pytest
from fastapi.testclient import TestClient


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from main import app  

client = TestClient(app)

@pytest.fixture
def user_data():
    return {
        "nome": "Lanna",
        "email": "lanna@test.com",
        "senha": "minhasenha123"
    }

def test_create_user(user_data):
    response = client.post("/users/users", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == user_data["nome"]
    assert data["email"] == user_data["email"]
    assert "id_usuario" in data

def test_login_user(user_data):
   
    client.post("/users/users", json=user_data)

    response = client.post(
        "/users/login",
        data={"username": user_data["email"], "password": user_data["senha"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_access_me_endpoint(user_data):
    
    client.post("/users/users", json=user_data)
    login_response = client.post(
        "/users/login",
        data={"username": user_data["email"], "password": user_data["senha"]}
    )
    token = login_response.json()["access_token"]

    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == user_data["nome"]
    assert data["email"] == user_data["email"]