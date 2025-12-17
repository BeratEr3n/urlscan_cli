# src/core/api.py

import requests
from typing import Optional, Dict
from config.settings import TIMEOUT


class APIClient:
    """
    urlscan.io API ile HTTP haberleşmesini yöneten katman.
    """

    BASE_URL = "https://urlscan.io/api/v1"

    def __init__(self, api_key: str, timeout: int = TIMEOUT):
        if not api_key:
            raise ValueError("api_key is required")

        self.api_key = api_key
        self.timeout = timeout

        self.headers = {
            "api-key": self.api_key,
            "User-Agent": "urlscan-cli/1.0"
        }


    def get(self, path: str, params: Optional[Dict] = None, raw: bool = False):
        """
        GET request gönderir.
        raw=True ise response.json() yerine response döner (png, text vs için).
        """
        url = f"{self.BASE_URL}{path}"

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=self.timeout
        )

        self._handle_errors(response)

        if raw:
            return response

        return response.json()


    def post(self, path: str, json: Optional[Dict] = None ) -> Dict:
        """
        POST request gönderir (JSON body).
        """
        url = f"{self.BASE_URL}{path}"

        headers = {
            **self.headers,
            "Content-Type": "application/json"
        }

        response = requests.post(
            url,
            headers=headers,
            json=json,
            timeout=self.timeout
        )

        self._handle_errors(response)
        return response.json()


    def _handle_errors(self, response: requests.Response):
        """
        Ortak HTTP hata yönetimi.
        """
        if response.status_code == 429:
            reset_after = response.headers.get("X-Rate-Limit-Reset-After")
            raise RuntimeError(
                f"Rate limit exceeded. Retry after {reset_after} seconds"
            )

        if response.status_code >= 400:
            try:
                data = response.json()
                message = data.get("message", "Unknown error")
                description = data.get("description", "")
                raise RuntimeError(
                    f"HTTP {response.status_code}: {message} {description}"
                )
            except ValueError:
                response.raise_for_status()
