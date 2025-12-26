# src/core/parser.py

class UrlScanResultParser:
    """
    urlscan.io result JSON'unu CLI için sadeleştiren parser.
    """

    def parse(self, result: dict) -> dict:
        task = result.get("task", {})
        page = result.get("page", {})
        verdicts = result.get("verdicts", {})
        lists = result.get("lists", {})

        urlscan_verdict = verdicts.get("urlscan", {})
        urlscan_verdict = verdicts.get("urlscan", {})
        overall_verdict = verdicts.get("overall", {})

        parsed = {
            "task": {
                "uuid": task.get("uuid"),
                "url": task.get("url"),
                "time": task.get("time"),
                "visibility": task.get("visibility"),
                "report_url": task.get("reportURL"),
            },
            "page": {
                "domain": page.get("domain"),
                "ip": page.get("ip"),
                "country": page.get("country"),
                "asn": page.get("asn"),
                "asn_name": page.get("asnname"),
                "server": page.get("server"),
                "title": page.get("title"),
            },
            "verdict": {
                "malicious": overall_verdict.get("malicious"),
                "score": urlscan_verdict.get("score"),
                "categories": urlscan_verdict.get("categories", []),
            },
            "observables": {
                "domains": lists.get("domains", [])[:20],
                "ips": lists.get("ips", [])[:20],
                "hashes": lists.get("hashes", [])[:20],
            },
        }
        import json
        json_output = json.dumps(parsed, indent=2, ensure_ascii=False)


        return json_output
    
class UrlScanSearchParser:

    def parse(self, result: dict):
        
        # TODO parse edilebilir
        parsed =  result

        import json
        json_output = json.dumps(parsed, indent=2, ensure_ascii=False)


        return json_output
