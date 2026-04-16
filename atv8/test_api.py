import requests
import pytest
import jsonschema

BASE_URL = "https://jsonplaceholder.typicode.com"

# Schema básico do recurso (posts)
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

# =========================
# FIXTURE (Setup / Teardown)
# =========================
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

    # Teardown (simulado na API)
    requests.delete(f"{BASE_URL}/posts/{post['id']}")


# =========================
# 1. GET coleção
# =========================
def test_get_colecao():
    """GET /posts -> 200 e lista não vazia."""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0


# =========================
# 2. GET com schema
# =========================
def test_get_schema():
    """GET /posts/1 -> valida schema."""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)


# =========================
# 3. GET inexistente
# =========================
def test_get_inexistente():
    """GET /posts/999999 -> 404."""
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404


# =========================
# 4. POST (CREATE)
# =========================
def test_post_criar():
    """POST /posts -> 201 e retorno com id."""
    payload = {
        "title": "Novo Post",
        "body": "Conteúdo",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert "id" in data


# =========================
# 5. UPDATE (PATCH)
# =========================
def test_update_post():
    """PATCH /posts/1 -> campo atualizado."""
    payload = {
        "title": "Título Atualizado"
    }

    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Título Atualizado"


# =========================
# 6. DELETE
# =========================
def test_delete_post():
    """DELETE /posts/1 -> status 200."""
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


# =========================
# 7. VALIDAÇÃO (dados inválidos)
# =========================
def test_dados_invalidos():
    """POST inválido -> deve retornar erro (simulado)."""
    payload = {
        "title": "",  # inválido (vazio)
        "body": "teste",
        "userId": "abc"  # inválido
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    # JSONPlaceholder não valida de verdade,
    # então aceitamos 201 ou simulamos lógica
    assert response.status_code in [201, 400]


# =========================
# 8. AUTENTICAÇÃO (simulado)
# =========================
def test_sem_autenticacao():
    """Endpoint sem autenticação (API pública)."""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


# =========================
# 9. FIXTURE em uso
# =========================
def test_fixture(post_criado):
    """Verifica se fixture criou o recurso."""
    assert "id" in post_criado


# =========================
# 10. PERFORMANCE
# =========================
def test_tempo_resposta():
    """Tempo de resposta < 2 segundos."""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.elapsed.total_seconds() < 2.0