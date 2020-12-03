import requests
from requests.exceptions import HTTPError
from .config import BASE_URL, AUTH_TOKEN


def acquire_problem_input() -> str:
    try:
        res = requests.get(
            url=BASE_URL,
            cookies={"session": AUTH_TOKEN},
        )
        res.raise_for_status()
        return res.text
    except HTTPError as err:
        print(err)
        raise