import pytest

# fixture for set
@pytest.fixture
def set_fixture():
    print('this is set fixture')

# fixture for list
@pytest.fixture
def list_fixture():
    print('this is list fixture')

class TestClass:






# fixture for dictionary
@pytest.fixture
def dictionary_fixture():
    print('this is dictionary fixture')

# fixture for string
@pytest.fixture
def string_fixture():
    print('this is string fixture')