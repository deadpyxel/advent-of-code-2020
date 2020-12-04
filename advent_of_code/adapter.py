import requests
from requests.exceptions import HTTPError

from .config import AUTH_TOKEN
from .config import BASE_URL


def acquire_problem_input(day: int = 1) -> str:
    try:
        res = requests.get(
            url=BASE_URL.replace("{}", str(day)),
            cookies={"session": AUTH_TOKEN},
        )
        res.raise_for_status()
        return res.text
    except HTTPError as err:
        print(err)
        raise
