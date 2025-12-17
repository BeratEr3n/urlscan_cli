# src/cli/parser.py

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="urlscan",
        description="urlscan.io CLI tool"
    )

    parser.add_argument(
        "--api-key",
        required=True,
        help="urlscan.io API key"
    )

    # ---- mode selection ----
    mode_group = parser.add_mutually_exclusive_group(required=True)

    mode_group.add_argument(
        "--scan",
        action="store_true",
        help="Submit a URL to urlscan and wait for result"
    )

    mode_group.add_argument(
        "--search",
        action="store_true",
        help="Search urlscan historical data"
    )

    # ---- common / scan args ----
    parser.add_argument(
        "--url",
        help="URL to scan or search"
    )

    parser.add_argument(
        "--visibility",
        choices=["public", "unlisted", "private"],
        default="public",
        help="Scan visibility (default: public)"
    )

    # ---- search args ----
    search_group = parser.add_mutually_exclusive_group()

    search_group.add_argument(
        "--domain",
        help="Search by domain"
    )

    search_group.add_argument(
        "--ip",
        help="Search by IP (IPv4 or IPv6)"
    )

    search_group.add_argument(
        "--hash",
        help="Search by file SHA256 hash"
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of search results"
    )

    return parser
