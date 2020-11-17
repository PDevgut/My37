import os
from framework.consts import USER_DATA_FILE
from framework.types import ResponseT
from framework.utils import build_status


def hello_reset(_request):
    if USER_DATA_FILE.is_file():
        os.remove(USER_DATA_FILE)
    response = ResponseT(
        status=build_status(302),
        headers={"Location": "/h/"},
    )

    return response