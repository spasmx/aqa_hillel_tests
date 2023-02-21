import pytest
import time


@pytest.mark.timed
def test_1():
    time.sleep(2)
    pass


@pytest.mark.xfail
@pytest.mark.timed
def test_2():
    time.sleep(2)
    assert True


@pytest.mark.timed
def test_3():
    time.sleep(2)
    assert True


@pytest.mark.timed
def test_4():
    time.sleep(2)
    assert True


@pytest.mark.timed
def test_5():
    time.sleep(2)
    assert True


@pytest.mark.xfail
@pytest.mark.timed
def test_6():
    time.sleep(2)
    assert True


@pytest.mark.timed
def test_7():
    time.sleep(2)
    assert True


@pytest.mark.timed
def test_8():
    time.sleep(2)
    assert True


@pytest.mark.timed
def test_9():
    time.sleep(2)
    assert True


@pytest.mark.timed
def test_10():
    time.sleep(2)
    assert True
