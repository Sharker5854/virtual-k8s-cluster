from math import pi
from flask import Flask, request


def parse_conf_file(path: str) -> dict:
    with open(path, "r") as conf_file:
        data = conf_file.read().split("\n")
        result = {}
        for pair in data:
            pair = pair.split("=")
            try:
                result[pair[0]] = pair[1]
            except IndexError:
                pass
        return result


app = Flask(__name__)
config: dict = parse_conf_file("/python-config/python_backend.params")

@app.route('/circle-area')
def circle_area_handler():
    try:
        radius = int(request.args.get(config.get("radius_query_param_name")))
    except:
        return 'Invalid radius parameter', 400
    area = calculate_area(radius)
    return f'Python: {round(area, int(config.get("float_precision")))}'

def calculate_area(radius):
    return pi * radius ** 2


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(config.get("flask_port")))