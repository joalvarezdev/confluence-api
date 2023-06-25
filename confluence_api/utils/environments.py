import os

from dotenv import load_dotenv

load_dotenv()

def get_url() -> str | None:
    return os.getenv("URL")


def get_user_email() -> str | None:
    return os.getenv("USERNAME")


def get_token() -> str | None:
    return os.getenv("TOKEN")


def get_docs_path() -> str | None:
    return os.getenv("FILES_PATH")
