import os

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.rq import RqIntegration

load_dotenv()

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN", ""),
    integrations=[
        RqIntegration(),
    ],
    environment=os.environ.get("ENVIRONMENT", ""),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)
