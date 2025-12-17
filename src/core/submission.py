# src/core/submission.py

from typing import Optional, List, Dict
from core.api import APIClient


class UrlScanSubmissionService:
    """
    urlscan.io Scan API üzerinden URL submit işlemini yapan servis.
    """

    def __init__(self, client: APIClient):
        self.client = client

    def submit(
        self,
        url: str,
        visibility: str = "public",
        tags: Optional[List[str]] = None,
    ) -> Dict:
        """
        URL'i urlscan'e gönderir ve scan UUID döner.

        :param url: Taranacak URL
        :param visibility: public | unlisted | private
        :param tags: kullanıcı tanımlı tag listesi (max 10)
        """

        payload: Dict = {
            "url": url,
            "visibility": visibility,
        }

        if tags:
            payload["tags"] = tags[:10]


        return self.client.post(
            path="/scan",
            json=payload
        )
