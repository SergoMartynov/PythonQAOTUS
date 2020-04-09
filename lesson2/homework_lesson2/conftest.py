import pytest

@pytest.fixture
def set_fixture():
    print('this is set fixture')

def list_fixture():
    print('this is list fixture')

def dictionary_fixture():
    print('this is dictionary fixture')

def string_fixture():
    print('this is string fixture')