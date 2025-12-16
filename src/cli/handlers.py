#src/cli/handler.py

from core.api import APIClient
from core.orchestrator import (
    UrlScanScanOrchestrator,
    UrlScanSearchOrchestrator
)
from core.classifier import TargetType


client = APIClient()

scan_orchestrator = UrlScanScanOrchestrator(client)
search_orchestrator = UrlScanSearchOrchestrator(client)


def handle_command(args):
    if args.command == "scan":
        handle_scan(args)
    elif args.command == "search":
        handle_search(args)
    else:
        raise RuntimeError("Unknown command")


def handle_scan(args):
    result = scan_orchestrator.run(
        url=args.url,
        visibility=args.visibility,
    )
    print(result)


def handle_search(args):
    if args.target:
        result = search_orchestrator.run_search(
            target=args.target,
            target_type=TargetType.TARGET,
            limit=args.limit,
        )

    elif args.domain:
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
