import sys
from cli.parser import build_parser
from cli.handlers import handle_command


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        handle_command(args)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
