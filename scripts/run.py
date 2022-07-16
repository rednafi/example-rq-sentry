from __future__ import annotations

import subprocess
import signal
from functools import partial
import sys

run = partial(subprocess.run, check=False, shell=True)


def setup() -> None:
    """Make sure you have Docker installed in your system.
    Start a Alpine Redis container.
    """
    # Some orphan processes might be left over from previous runs.
    teardown()
    run("docker run --name dev-redis -d -h localhost -p 6379:6379 redis:7-alpine")


def teardown() -> None:
    run("pkill app.scheduler")
    run("pkill app.worker")
    run("docker stop dev-redis")
    run("docker rm dev-redis")


def orchestrate():
    try:
        setup()

        # Run the scheduler in the background.
        run("python -m app.scheduler &", check=True)

        # Run the worker in the background.
        # The worker will listen for jobs on the default queue.
        run("python -m app.worker &", check=True)

        signal.pause()
    finally:
        print("Got interrupted, tearing down...")
        teardown()
        sys.exit(0)


if __name__ == "__main__":
    orchestrate()
