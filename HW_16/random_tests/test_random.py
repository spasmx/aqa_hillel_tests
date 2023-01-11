import pytest


@pytest.mark.pack
@pytest.mark.joint
def test_sum():
    print('test sum')
    result = 1 + 1
    assert result == 2


@pytest.mark.pack
@pytest.mark.joint
def test_random():
    print('test random')
    pass


@pytest.mark.pack
@pytest.mark.rest
def test_bool():
    print('test bool')
    assert True
