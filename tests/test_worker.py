from unittest.mock import Mock, patch

from app import worker


@patch.object(worker, "capture_exception", autospec=True)
def test_handle_exception(mock_capture_exception):
    mock_job = Mock()
    mock_exc_type = Mock()
    mock_exc_value = Mock()
    mock_traceback = Mock()
    result = worker.handle_exception(
        mock_job,
        mock_exc_type,
        mock_exc_value,
        mock_traceback,
    )

    assert result is False
    mock_capture_exception.assert_called_once_with(mock_exc_value)


def test_run_worker():
    with patch.object(worker, "Worker", autospec=True) as mock_worker:
        worker.run_worker()
        mock_worker.assert_called_once_with(
            queues=["default"],
            exception_handlers=[worker.handle_exception],
            disable_default_exception_handler=True,
        )
        mock_worker.return_value.work.assert_called_once_with(with_scheduler=True)
