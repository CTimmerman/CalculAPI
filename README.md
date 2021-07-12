# CalculAPI
Simple calculator JSON REST API.

## Usage

Valid equations return code 200 and the result:

    http://localhost:8888/?q={"q":"sqrt(e)-log(pi)"}

    {"result": 0.503991384850728}

    http://localhost:8888/?q={"q":"1 - 2 / 6"}

    {"result": 0.6666666666666667}

JSON via POST is easier via the terminal:

    curl 127.0.0.1:8888 -d {"q":"1 - 2 / 6"}

    {"result": 0.6666666666666667}

Invalid equations return code 400 and the reason as result:

    http://localhost:8888/?q={"q":"1 - 2 / b6"}

    {"result": "Invalid equation. Should match ^([ 0-9.()^|*/%+-]|acos|acosh|asin|asinh|atan|atan2|atanh|ceil|comb|copysign|cos|cosh|degrees|dist|e|erf|erfc|exp|expm1|fabs|factorial|floor|fmod|frexp|fsum|gamma|gcd|hypot|inf|isclose|isfinite|isinf|isnan|isqrt|ldexp|lgamma|log|log10|log1p|log2|modf|nan|perm|pi|pow|prod|radians|remainder|sin|sinh|sqrt|tan|tanh|tau|trunc)+$."}

## Installation

    docker build calculapi .
    docker run -dp 8888:8888 calculapi
