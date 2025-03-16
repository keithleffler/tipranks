from tipranks.errors import (
    TipRanksStatusCodeError,
    TipRanksArgumentError,
    TipRanksRequestError
)
from typing import Optional, Any
import requests

class TrClient:
    def __init__(self, email: str, password: str) -> None:
        self._base_url: str = "https://www.tipranks.com"
        self._session: requests.sessions.Session = requests.Session()

        self.login(email=email, password=password)

    def request(
            self, method: str, endpoint: str, params: Optional[dict] = None, json: Optional[dict] = None, login: Optional[bool] = None
    ) -> Any:
        try:
            response = self._session.request(
                method=method.upper(),
                url=f"{self._base_url}{endpoint}",
                headers={
                    "accept": "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "content-type": "application/json; charset=UTF-8",
                    "accept-encoding": "gzip",
                    "x-platform": "iphone",
                    "user-agent": "TipRanksApp/17 CFNetwork/1390 Darwin/22.0.0",
                    "accept-language": "en-US,en;q=0.9"
                },
                json=json,
                params=params
            )
        except:
            raise TipRanksRequestError("Request Timed Out")

        if login:
            return response.status_code
        try:
            return response.json()
        except :
            return response

    def login(self, email: str, password: str) -> None:
        status_code = self.request(
            method="POST",
            endpoint="/api/iOS/login2",
            json={
                "email": email,
                "password": password
            },
            login=True
        )

        if status_code != 200:
            raise TipRanksStatusCodeError(f"Failed To Login, Status Code: {status_code}")
