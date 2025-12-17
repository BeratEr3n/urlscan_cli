# src/core/orchestrator.py

from core.submission import UrlScanSubmissionService
from core.poller import UrlScanPoller
from core.parser import UrlScanResultParser
from core.search import UrlScanSearchService
from core.classifier import TargetType


class UrlScanScanOrchestrator:
    """
    urlscan scan akışını uçtan uca yöneten katman.
    """

    def __init__(self, client):
        self.submission = UrlScanSubmissionService(client)
        self.poller = UrlScanPoller(client)
        self.parser = UrlScanResultParser()

    def run(
        self,
        url: str,
        visibility: str = "public",
    ) -> dict:
        # 1. submit
        submit_resp = self.submission.submit(
            url=url,
            visibility=visibility,
        )

        scan_id = submit_resp.get("uuid")
        if not scan_id:
            raise RuntimeError("Scan submission did not return uuid")

        # 2. poll
        result = self.poller.wait(scan_id)

        # 3. parse
        #return self.parser.parse(result)
        return result



class UrlScanSearchOrchestrator:
    """
    Search akışını yöneten orchestration katmanı.
    target_type kararına göre SearchService çağırır.
    """

    def __init__(self, client):
        self.search = UrlScanSearchService(client)

    def run_search(
        self,
        target: str,
        target_type: TargetType,
        limit: int | None = None,
    ) -> dict:
        
        # auto-detect (--target)
        if target_type == TargetType.TARGET:
            detected = self.search.detect_target_type(target)
            return self.search.search(
                target=target,
                target_type=detected,
                limit=limit,
            )

        # explicit (--domain, --ip, --url, --hash)
        return self.search.search(
            target=target,
            target_type=target_type,
            limit=limit,
        )
