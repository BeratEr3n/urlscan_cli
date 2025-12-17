# src/core/search.py

from typing import Dict
from core.api import APIClient
from core.classifier import TargetType
from config.settings import SEARCH_RESULT_LIMIT


class UrlScanSearchService:
    """
    urlscan.io Search API üzerinden lookup (search) yapan servis.
    """

    def __init__(self, client: APIClient):
        self.client = client


    def _build_query(self, target: str, target_type: TargetType) -> str:
        """
        TargetType'a göre Elasticsearch query string üretir.
        """

        if target_type == TargetType.DOMAIN:
            return f"page.domain:{target}"

        if target_type == TargetType.IP:
            return f'page.ip:"{target}"'

        if target_type == TargetType.URL:
            return f'task.url:"{target}"'

        if target_type == TargetType.HASH:
            # urlscan sadece indirilen dosyaların hash'lerini bilir
            return f"files.sha256:{target}"

        raise ValueError(f"Unsupported target type: {target_type}")

    def search(
        self,
        target: str,
        target_type: TargetType,
        limit: int | None = None,
    ) -> Dict:
        """
        Belirtilen target ve target_type'a göre arama yapar.
        """
        size = limit or SEARCH_RESULT_LIMIT

        query = self._build_query(target, target_type)

        params = {
            "q": query,
            "size": size,
            "datasource": "scans"
        }

        return self.client.get(
            path="/search",
            params=params
        )
