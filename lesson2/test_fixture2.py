def test_the_class(fixture_return_rnd_number):
    assert fixture_return_rnd_number == 20


def test_the_class(fixture_return_class):
    assert fixture_return_class.mod2.pow(2, 3) == 8
    assert fixture_return_class.mod1.choice(['a', 'b', 'c']) == 'a'

def test_the_class2(first_fixture_return_class):
    assert first_fixture_return_class.hello('Ivan') == 'Hello, Ivan'

@pytest.fixture(scope='session')
def session_fixture(request):
    print(f"\n тестовое говно")

@pytest.fixture
def fixture_one():
    print()

@pytest.fixture
def fixture_two():
    print()

# параметризация
