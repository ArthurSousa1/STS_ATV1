import requests
import pytest
import jsonschema

BASE_URL = "https://jsonplaceholder.typicode.com"

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "body", "userId"],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"}
    }
}

@pytest.fixture
def post_criado():
    """Cria um post antes do teste e remove depois."""
    payload = {
        "title": "Post Teste",
        "body": "Conteúdo teste",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

    post = response.json()
    yield post

    requests.delete(f"{BASE_URL}/posts/{post['id']}")


def test_get_colecao():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_schema():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)


def test_get_inexistente():
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404

def test_post_criar():
    payload = {
        "title": "Novo Post",
        "body": "Conteúdo",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert "id" in data

def test_update_post():
    payload = {
        "title": "Título Atualizado"
    }

    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Título Atualizado"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_dados_invalidos():
    payload = {
        "title": "",  
        "body": "teste",
        "userId": "abc" 
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code in [201, 400]

def test_sem_autenticacao():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_fixture(post_criado):
    assert "id" in post_criado

def test_tempo_resposta():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.elapsed.total_seconds() < 2.0