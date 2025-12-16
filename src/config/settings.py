# urlscan_cli/config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("URLSCAN_API_KEY")

SEARCH_RESULT_LIMIT = int(20)

# Timeout
TIMEOUT = int(60)
POLL_TIMEOUT = TIMEOUT*2

SCAN_INTERVAL = int(5)
SCAN_TIMEOUT = TIMEOUT*5

