import dataclasses
import json

from framework.consts import USER_DATA_FILE
from framework.types import RequestT, UserDataT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static

def handle_hello(request: RequestT) -> ResponseT:
    if request.method == "GET":
        return handle_hello_get(request)
    else:
        return handle_hello_post(request)

def handle_hello_get(request: RequestT) -> ResponseT:
    assert request.method == "GET"

    base = read_static("_base.html")
    base_html = base.content.decode()
    hello_html = read_static("hello.html").content.decode()

    user_data = load_user_data(request)

    document = hello_html.format(
        address_header=user_data.address or "nowhere",
        address_value=user_data.address or "",
        name_header=user_data.name or "Bro",
        name_value=user_data.name or "",
    )
    document = base_html.format(xxx=document)

    resp = ResponseT(
        status=build_status(200),
        headers={"Content-Type": base.content_type},
        payload=document.encode(),
    )

    return resp

def handle_hello_post(request: RequestT) -> ResponseT:
    assert request.method == "POST"

    form_data = request.form_data

    name = form_data.get("name", [None])[0]
    address = form_data.get("address", [None])[0]

    user_data = UserDataT(name=name, address=address)

    save_user_data(user_data)

    response = ResponseT(
        status=build_status(302),
        headers={"Location": "/h/"},
    )

    return response

def save_user_data(user_data: UserDataT) -> None:
    user_data_dct = dataclasses.asdict(user_data)
#    user_id = build_users_id(request)
    with USER_DATA_FILE.open("w") as fp:
        json.dump(user_data_dct, fp, sort_keys=True, indent=2)


def load_user_data(request: RequestT) -> UserDataT:
    if not USER_DATA_FILE.is_file():
        return UserDataT()

    with USER_DATA_FILE.open("r") as fp:
        users_data_dct = json.load(fp)

    user_data = UserDataT(**users_data_dct)
    return user_data
