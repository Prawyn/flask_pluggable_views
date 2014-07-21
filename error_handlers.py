from flask import render_template, jsonify

from routing import app
from myexceptions import *

#Error Handlers

@app.errorhandler(404)
def unexpected_error(error):
    """ error handler for unknown error """
    return render_template('error.html'), 404


@app.errorhandler(AuthenticationException)
def auth_error(error):
    """ error handler user entered data exception """
    return jsonify({'error': error.get_message()})