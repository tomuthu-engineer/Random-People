from flask import request, render_template


def upload_controller():
    try:
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            pass
        else:
            pass
    except Exception as error:
        return render_template('500.html')
    

def view_user_controller():
    try:
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            pass
        else:
            pass
    except Exception as error:
        return render_template('500.html')
    

def play_view_controller():
    try:
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            pass
        else:
            pass
    except Exception as error:
        return render_template('500.html')