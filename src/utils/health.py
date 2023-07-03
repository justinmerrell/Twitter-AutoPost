import os
import logging

import requests

logger = logging.getLogger("tweet")

HEALTH_URL = os.getenv("HEALTHCHECKS_URL", "http://localhost:8000/health")
HEALTH_ID = os.getenv("HEALTHCHECKS_ID", None)


def send_healthcheck(fail=False):
    '''
    Send a healthcheck to healthchecks
    '''
    if HEALTH_ID is None:
        logging.warning("No healthcheck ID provided. Skipping healthcheck.")
        return

    if fail:
        logging.info("Sending failed healthcheck.")
        requests.get(f"{HEALTH_URL}/{HEALTH_ID}/fail")
        return

    logging.info("Sending successful healthcheck.")
    requests.get(f"{HEALTH_URL}/{HEALTH_ID}", timeout=5)
