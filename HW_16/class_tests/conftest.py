import pytest


@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    print('START TEST')
    yield
    print('END TEST')
