#src/cli/handler.py

from core.api import APIClient
from core.orchestrator import (
    UrlScanScanOrchestrator,
    UrlScanSearchOrchestrator
)
from core.classifier import TargetType


def handle_command(args):
    client = APIClient(api_key=args.api_key)

    scan_orchestrator = UrlScanScanOrchestrator(client)
    search_orchestrator = UrlScanSearchOrchestrator(client)

    if args.command == "scan":
        handle_scan(args, scan_orchestrator)
    elif args.command == "search":
        handle_search(args, search_orchestrator)
    else:
        raise RuntimeError("Unknown command")



def handle_scan(args, scan_orchestrator):
    result = scan_orchestrator.run(
        url=args.url,
        visibility=args.visibility,
    )
    print(result)


def handle_search(args, search_orchestrator):
    if args.domain:
        result = search_orchestrator.run_search(
            target=args.domain,
            target_type=TargetType.DOMAIN,
            limit=args.limit,
        )

    elif args.ip:
        result = search_orchestrator.run_search(
            target=args.ip,
            target_type=TargetType.IP,
            limit=args.limit,
        )

    elif args.url:
        result = search_orchestrator.run_search(
            target=args.url,
            target_type=TargetType.URL,
            limit=args.limit,
        )

    elif args.hash:
        result = search_orchestrator.run_search(
            target=args.hash,
            target_type=TargetType.HASH,
            limit=args.limit,
        )

    else:
        raise RuntimeError("No valid search argument provided")

    print(result)
