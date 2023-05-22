#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return f"{parameter}"


@app.route("/count/<int:parameter>")
def count(parameter):
    counted = [i for i in range(parameter)]
    results = "\n".join(str(num) for num in counted) + "\n"
    return results


@app.route("/math/<int:num>/<string:operation>/<int:num2>")
def math(num, operation, num2):
    if operation == "+":
        sum = num + num2
        return str(sum)
    elif operation == "-":
        result = num - num2
        return str(result)
    elif operation == "*":
        product = num * num2
        return str(product)
    elif operation == "%":
        quotient = num % num2
        return str(quotient)
    elif operation == "div":
        quotient = num / num2
        return str(quotient)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
