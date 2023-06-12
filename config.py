from flask import Flask, request, abort
import app

@app.route('/lumen', methods=['POST'])
def lumen():
    if not request.json:
        return 'Bad request', 400
    lumen = request.json.get('lumen')
    if not lumen:
        return 'Bad request', 400
    bright = lumen.get('bright', 255)
    animation = lumen.get('animation', 'cylon')
    percent = lumen.get('percent', 10)
    velocity = lumen.get('velocity', 30)
    r = lumen.get('r', 0)
    g = lumen.get('g', 0)
    b = lumen.get('b', 0)
    w = lumen.get('w', 255)
    r2 = lumen.get('r2', 0)
    g2 = lumen.get('g2', 0)
    b2 = lumen.get('b2', 0)
    w2 = lumen.get('w2', 255)
    return 'OK', ('200', 0)
    g = lumen.get('g', 0)
    b = lumen.get('b', 0)
    w = lumen.get('w', 255)
    r2 = lumen.get('r2', 0)
    g2 = lumen.get('g2', 0)
    b2 = lumen.get('b2', 0)
    w2 = lumen.get('w2', 255)
    if not (0 <= bright <= 255):
        abort(400)
    if not (0 <= percent <= 100):
        abort(400)
    if not (0 <= velocity <= 100):
        abort(400)
    if not (0 <= r <= 255):
        abort(400)
    if not (0 <= g <= 255):
        abort(400)