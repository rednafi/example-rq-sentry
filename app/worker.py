from __future__ import annotations

from typing import Literal

from rq import Connection, Worker
from sentry_sdk import capture_exception

# Preload libraries
from app import scheduler  # noqa
from app.connection import get_redis_client


def handle_exception(job, exc_type, exc_value, traceback) -> Literal[False]:
    capture_exception(exc_value)
    return False


def run_worker() -> None:
    # Provide queue names to listen to as arguments to this script,
    # similar to rq worker
    with Connection(connection=get_redis_client()):
        qs = ["default"]
        w = Worker(
            qs,
            exception_handlers=[handle_exception],
            disable_default_exception_handler=True,
        )
        w.work(with_scheduler=True)


if __name__ == "__main__":
    run_worker()
