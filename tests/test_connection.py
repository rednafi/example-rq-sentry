from unittest.mock import patch

from app import connection


@patch.object(connection, "redis", autospec=True)
def test_get_redis_client(mock_redis):
    mock_redis_client = connection.get_redis_client()
    mock_redis.from_url.assert_called_once_with("redis://localhost:6379/0")
    assert mock_redis_client is mock_redis.from_url.return_value
    assert connection._cache == {"redis://localhost:6379/0": mock_redis_client}
