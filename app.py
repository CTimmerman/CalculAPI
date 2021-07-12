"""A simple calculator JSON REST API."""

import json, logging, math, re
from wsgiref.simple_server import make_server

from pyramid.config import Configurator


VALID_PATTERN = (
    f"^([ 0-9.()^|*/%+-]|{'|'.join(name for name in dir(math) if '_' not in name)})+$"
)
PORT = 8888


def calc(request):
    """
    >>> from pyramid.testing import DummyRequest
    >>> calc(DummyRequest(json_body={'q':'pi / (1+1)'}, method='POST')).body
    b'{"result": 1.5707963267948966}'
    >>> calc(DummyRequest(json_body={'q':'pi / (1+1) / hax'}, method='POST')).status
    '400 Bad Request'
    """
    try:
        q_param = request.params.get("q")
        if q_param:
            equation = json.loads(q_param)["q"]
        else:
            equation = request.json_body["q"]
        logging.debug(f"Equation: {equation}")
        if re.match(VALID_PATTERN, equation):
            result = eval(equation, math.__dict__)
        else:
            result = f"Invalid equation. Should match {VALID_PATTERN}."
            request.response.status = 400
    except Exception as e:
        result = json.dumps(str(e))
        request.response.status = 400

    logging.debug(result)
    request.response.body = json.dumps({"result": result}).encode("utf8")
    request.response.content_type = "application/json"
    return request.response


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("calc", "/")
        config.add_view(calc, route_name="calc")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", PORT, app)
    logging.debug(f"Listening on {PORT} for {VALID_PATTERN}")
    server.serve_forever()
