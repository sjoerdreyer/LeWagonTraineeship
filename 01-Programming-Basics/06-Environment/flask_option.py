# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    if os.getenv('FLASK_ENV'):
        return f"Starting in {os.getenv('FLASK_ENV')} mode..."
    return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
