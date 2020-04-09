import pytest

# --fixtures
@pytest.fixture
def first_fixture():
    print("\n===> Print from 'first'")
    """
    
    
    :return: 
    """

def test_first():
    a = 3
    b = 3
    assert a + b == 6
    assert a - b == 0

def test1():
    assert 2 + 2 == 4

class TestClass:

# создание тестовых файлов
    def test_one(self):
        print('I am test one')
        list_to_test1 = [1, 2]
        list_to_test2 = [1, 2]
        assert list_to_test1 is list_to_test2

    def test_two(self):
        assert 1 is 1