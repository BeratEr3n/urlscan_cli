#src/cli/parser.py

import argparse

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="urlscan",
        description="urlscan.io CLI tool"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ----------------- scan -----------------
    scan = subparsers.add_parser(
        "scan",
        help="Submit a URL to urlscan and wait for result"
    )

    scan.add_argument(
        "--url",
        required=True,
        help="URL to scan"
    )

    scan.add_argument(
        "--visibility",
        choices=["public", "unlisted", "private"],
        default="public",
        help="Scan visibility (default: public)"
    )

    # ----------------- search -----------------
    search = subparsers.add_parser(
        "search",
        help="Search urlscan historical data"
    )

    search_group = search.add_mutually_exclusive_group(required=True)

    search_group.add_argument(
        "--target",
        help="Auto-detect target type (domain, ip, url, hash)"
    )

    search_group.add_argument(
        "--domain",
        help="Search by domain"
    )

    search_group.add_argument(
        "--ip",
        help="Search by IP (IPv4 or IPv6)"
    )

    search_group.add_argument(
        "--url",
        help="Search by URL"
    )

    search_group.add_argument(
        "--hash",
        help="Search by file SHA256 hash"
    )

    search.add_argument(
        "--limit",
        type=int,
        help="Limit number of search results"
    )

    return parser
