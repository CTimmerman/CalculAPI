# CalculAPI
Simple calculator JSON REST API.

## Usage

Valid equations return code 200 and the result:

    http://localhost:8888/?q={%22q%22:%221%20-%202%20/%206%22}

    {"result": 0.6666666666666667}

Invalid equations return code 400 and the reason as result:

    http://localhost:8888/?q={%22q%22:%221%20-%202%20/%20b6%22}

    {"result": "Invalid equation. Characters should match ^[ 0-9.()*/+-]*$."}

JSON via POST is easier via the terminal:

    curl 127.0.0.1:8888 -d '{"q": "1+1"}'

    {"result": 2}

## Installation

    docker build calculapi .
    docker run -dp 8888:8888 calculapi
