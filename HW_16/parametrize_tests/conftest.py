import pytest


@pytest.fixture(scope='function')
def function_fixture():
    print('\nSTART PARAM TEST')
    yield
    print('\nEND PARAM TEST')
