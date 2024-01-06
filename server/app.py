#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)
    return f'<h1>{string_param}</h1>'

@app.route('/count/<int_param>')
def count(int_param):
    numbers = '\n'.join(str(i) for i in range(1, int_param + 1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h1>Cannot divide by zero!</h1>'
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h1>Invalid operation</h1>'

    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5555)
