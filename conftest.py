import pytest

@pytest.fixture
def first_fixture():
    print("print from first_fixture")

@pytest.fixture
def fixture_return_numbers():
    list_03 = [10, 20, 30]
    return list_03
