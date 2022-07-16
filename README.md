# Add Sentry to custom RQ worker script

If you need to write a custom worker script for your async task service that uses Python
[RQ][1], adding Sentry to it can be a little tricky. Whenever I initialized `sentry-sdk`
according to the [docs][2], it'd only send exception events from the main process; not
from the worker processes.

This can be a problem because RQ forks multiple processes to execute tasks
asynchronously. If we can't send exception events from those processes, it defeats the
purpose of integrating Sentry into the stack. This repo demonstrates a way to send
exception events from the worker processes.

[1]: https://python-rq.org/
[2]: https://docs.sentry.io/platforms/python/guides/rq/
