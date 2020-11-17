import re
from typing import Dict
from typing import Tuple

from framework.types import HandlerT

from . import special
from .error import handle_error
from .hello import handle_hello
from .hello_reset import hello_reset
from .index import handle_index

urlpatterns: Dict[re.compile, HandlerT] = {
    re.compile(_path_pattern): _handler
    for _path_pattern, _handler in {
        "^/$": handle_index,
        "^/e/$": handle_error,
        "^/h/$": handle_hello,
        "^/s/(?P<file_name>.+)$": special.handle_static,
        "^/submit/$": handle_hello,
        "^/reset/$": hello_reset,
    }.items()
}


def get_handler_and_kwargs(path: str) -> Tuple[HandlerT, dict]:
    handler = special.handle_404
    kwargs = {}

    for current_path_regex, current_handler in urlpatterns.items():
        if match := current_path_regex.match(path):
            handler = current_handler
            kwargs = match.groupdict()
            break

    return handler, kwargs
