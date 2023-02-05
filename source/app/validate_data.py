import argparse
from defines import OPERATORS


def validate_arguments(parser: argparse.Namespace) -> bool:
    if parser.operator not in OPERATORS:
        print(f"Unsupported operator {parser.operator}")
        return False
    if parser.start_time > 59 or parser.start_time < 0:
        print("Start time must be in range 0-59")
        return False
    if parser.interval > 55 or parser.interval < 5:
        print("Interval must be in range 5-55")
        return False
    return True

