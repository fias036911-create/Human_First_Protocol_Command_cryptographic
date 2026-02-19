"""Command-line interface for basic Human First Protocol operations."""

import argparse
import sys
from pathlib import Path

from human_first_protocol import timestamp


def main() -> int:
    parser = argparse.ArgumentParser(description="Human First Protocol utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    ts = sub.add_parser("timestamp", help="create a timestamp receipt")
    ts.add_argument("file", type=Path, help="file to timestamp")

    vr = sub.add_parser("verify", help="verify a timestamp receipt")
    vr.add_argument("receipt", type=Path, help=".ots receipt file to verify")

    args = parser.parse_args()

    try:
        if args.command == "timestamp":
            receipt = timestamp.timestamp_file(args.file)
            print(f"Receipt written to {receipt}")
        elif args.command == "verify":
            ok = timestamp.verify_receipt(args.receipt)
            sys.exit(0 if ok else 1)
    except Exception as exc:
        parser.error(str(exc))

    return 0


if __name__ == "__main__":
    sys.exit(main())
