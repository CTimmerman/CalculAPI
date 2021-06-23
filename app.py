"""A simple calculator JSON REST API."""

import json, re
from wsgiref.simple_server import make_server
from pyramid.config import Configurator


VALID_PATTERN = "^[ 0-9.()*/+-]*$"


def calc(request):
    try:
        equation = json.loads(request.params.get("q"))["q"]
        if re.match(VALID_PATTERN, equation):
            result = eval(equation)
        else:
            result = f"Invalid equation. Characters should match {VALID_PATTERN}."
            request.response.status = 400
    except Exception as e:
        result = json.dumps(str(e))
        request.response.status = 400

    print(result)
    request.response.body = json.dumps({"result": result}).encode("utf8")
    request.response.content_type = "application/json"
    return request.response


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("calc", "/")
        config.add_view(calc, route_name="calc")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 8888, app)
    server.serve_forever()
