import sys
import requests
import pytest

def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__

if __name__ == "__main__":
    print(f"Python Version: {python_version()}")
    print(f"Requests Version: {requests_version()}")
    print(f"Pytest Version: {pytest_version()}")
