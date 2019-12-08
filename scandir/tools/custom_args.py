from argparse import ArgumentParser, Namespace
from typing import NewType, Any


def create_custom_args() -> NewType('Namespace', Any):
    parser = ArgumentParser()
    parser.add_argument("-d", "--dest", help="Enter what folder you need to scan")
    return parser.parse_args()
