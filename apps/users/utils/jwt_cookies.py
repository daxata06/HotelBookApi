from rest_framework import response
from settings.settings import SIMPLE_JWT


def set_jwt_cookies(
    response: response.Response, access_token: str, refresh_token: str
) -> response.Response:
    response.set_cookie(
        "access_token",
        access_token,
        max_age=SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
        httponly=True,
        samesite="Strict",
    )
    response.set_cookie(
        "refresh_token",
        refresh_token,
        max_age=SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
        httponly=True,
        samesite="Strict",
    )
    return response
