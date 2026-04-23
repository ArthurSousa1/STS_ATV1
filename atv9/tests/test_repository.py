import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository


@pytest.fixture
def mock_storage():
    return Mock()


@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Desc", Priority.BAIXA, prazo)


def test_save_atribui_id(repo, task):
    resultado = repo.save(task)
    assert resultado.id == 1


def test_save_chama_storage_add(repo, task, mock_storage):
    repo.save(task)
    mock_storage.add.assert_called_once_with(1, task)


def test_find_by_id_stub(repo, task, mock_storage):
    mock_storage.get.return_value = task
    resultado = repo.find_by_id(1)
    assert resultado == task


def test_sequencia_save_e_find(repo, task, mock_storage):
    repo.save(task)
    mock_storage.get.return_value = task

    resultado = repo.find_by_id(1)
    assert resultado == task


def test_find_all_vazio(repo, mock_storage):
    mock_storage.get_all.return_value = []
    resultado = repo.find_all()
    assert resultado == []