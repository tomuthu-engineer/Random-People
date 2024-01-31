from . import app
from .models import Participant
from flask import request, render_template
from .controller import (
    upload_controller, 
    view_user_controller,
    play_view_controller,
    empty_user_controller,
    index_controller
)


@app.route('/', methods=['GET'])
def index():
    return index_controller()

@app.route('/upload', methods=['GET', "POST"])
def upload():
    return upload_controller()


@app.route("/viewParticipate", methods=['POST', "GET"])
def view_user():
    return view_user_controller()

@app.route('/emptyTable', methods=['POST'])
def empty_user():
    return empty_user_controller()


@app.route('/play', methods=['GET', 'POST'])
def play_view():
    return play_view_controller()
