import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--test_args",
        action="store",
        default="",
    )