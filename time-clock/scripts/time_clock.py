#!/usr/bin/env python3
"""
The Time Clock - Factory attendance system.

Records work. Not meaning. Just presence.
"""

import argparse
from datetime import datetime
from pathlib import Path


def get_timestamp():
    """Get current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")


def format_entry(unit_id, message):
    """Format log entry."""
    timestamp = get_timestamp()
    return f"{timestamp} - [{unit_id}] {message}"


def append_to_ledger(ledger_path, entry):
    """Append entry to factory ledger."""
    ledger_file = Path(ledger_path)

    # Create file if it doesn't exist
    if not ledger_file.exists():
        ledger_file.parent.mkdir(parents=True, exist_ok=True)
        # Write header
        with open(ledger_file, "w") as f:
            f.write("# Factory Ledger\n\n")
            f.write("**Work log. Time record. Proof of operation.**\n\n")
            f.write("---\n\n")

    # Append entry
    with open(ledger_file, "a") as f:
        f.write(entry + "\n")


def clock_in(ledger_path, unit_id, message, silent=False):
    """Clock in. Record work. Continue."""

    # Format entry
    entry = format_entry(unit_id, message)

    # Write to ledger
    append_to_ledger(ledger_path, entry)

    # Confirm (unless silent)
    if not silent:
        print(entry)
        print("\nClocked in. Work recorded.")


def main():
    parser = argparse.ArgumentParser(
        description="The Time Clock - Factory attendance system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Work logged. Process continues."
  %(prog)s "Campbell's Soup Can #0042 produced."
  %(prog)s "Code written. Tests pass." --unit-id "Unit 07"
  %(prog)s "Repository recorded." --ledger-path ./warehouse/ledger.md
        """,
    )

    parser.add_argument(
        "message",
        help="Work message to log",
    )

    parser.add_argument(
        "--ledger-path",
        default="factory_ledger.md",
        help="Path to factory ledger (default: factory_ledger.md)",
    )

    parser.add_argument(
        "--unit-id",
        default="Unit 04",
        help="Unit identifier (default: Unit 04)",
    )

    parser.add_argument(
        "--silent",
        action="store_true",
        help="Silent mode (no output)",
    )

    args = parser.parse_args()

    clock_in(
        ledger_path=args.ledger_path,
        unit_id=args.unit_id,
        message=args.message,
        silent=args.silent,
    )


if __name__ == "__main__":
    main()
