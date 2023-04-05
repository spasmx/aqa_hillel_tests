import unittest
from unittest.mock import Mock


def process_data():
    try:
        pass
    except Exception as e:
        pass


def test_process_data():
    mock_funk = Mock(side_effect=Exception('Test exception'))
    mock_funk()






