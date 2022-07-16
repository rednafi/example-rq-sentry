from __future__ import annotations

import decimal
import time
from typing import TypeVar

import rq

RealNum = TypeVar("RealNum", int, float, decimal.Decimal)


def slow_add(a: RealNum, b: RealNum) -> RealNum:
    """Mimick a long-running async task."""

    print("Sleeping for 1 seconds")
    time.sleep(1)

    result = a + b

    # We intentionally fail the task to send the traceback to Sentry.
    1 / 0

    print(f"Returning result: {result}")
    return result


def schedule(q: rq.Queue[RealNum], a: RealNum, b: RealNum) -> RealNum:
    """Schedule a task to be run in the background."""

    # Retry 3 times if the task fails.
    job = q.enqueue(slow_add, a, b, retry=rq.Retry(3))
    return job.result
