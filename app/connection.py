from __future__ import annotations

import redis

_cache = {}


def get_redis_client(url: str = "redis://localhost:6379/0") -> redis.Redis:
    if url not in _cache:
        _cache[url] = redis.from_url(url)
    return _cache[url]
