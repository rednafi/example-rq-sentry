from unittest.mock import ANY, Mock, patch

import pytest

from app import tasks


@patch.object(tasks.time, "sleep", autospec=True)
def test_slow_add(mock_sleep):
    with pytest.raises(ZeroDivisionError):
        tasks.slow_add(1, 2)
    mock_sleep.assert_called_once_with(1)


def test_schedule():
    mock_q = Mock()
    mock_q.enqueue.return_value = Mock()
    tasks.schedule(mock_q, 1, 2)
    mock_q.enqueue.assert_called_once_with(tasks.slow_add, 1, 2, retry=ANY)
