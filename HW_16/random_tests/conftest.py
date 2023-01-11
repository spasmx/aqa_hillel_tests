import pytest


@pytest.fixture(scope='function', autouse=True)
def random_fixture():
    print('START')
    yield
    print('END')

