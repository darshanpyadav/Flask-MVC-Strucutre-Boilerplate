# -*- coding: utf-8 -*-
from src.app import app
from flask import session, request, abort
import random, string


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(30))
    return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token

from . import homeController