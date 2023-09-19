import pytest

'''
Tests in this file (with that specific name) are run before every test case.
Thus, I moved backend and request blocker here.
'''


@pytest.fixture()
def prepare_backend_file(tmpdir):
    temp_file = tmpdir.join('test.txt')
    temp_file.write('')
    return temp_file


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr('requests.sessions.Session.request')
