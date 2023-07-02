import os

import requests

HEALTH_URL = os.getenv("HEALTHCHECKS_URL", "http://localhost:8000/health")
HEALTH_ID = os.getenv("HEALTHCHECKS_ID", None)
