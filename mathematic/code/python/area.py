from math import pi
from flask import Flask, request


app = Flask(__name__)

@app.route('/circle-area')
def circle_area_handler():
    try:
        radius = int(request.args.get('radius'))
    except:
        return 'Invalid radius parameter', 400
    area = calculate_area(radius)
    return f'Python: {area:.6f}'

def calculate_area(radius):
    return pi * radius ** 2


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)