from flask import render_template, request
from .models import db, Participant
from io import TextIOWrapper
import pandas as pd
from . import app
from sqlalchemy import func


def upload_controller():
    if request.method == 'POST':
        try:
            file = request.files['file']
            filename = file.filename
            # Check if the file is a CSV file
            if filename and filename.endswith('.csv'):
                # Read the CSV file using pandas
                csv_file = TextIOWrapper(file.stream._file, encoding='utf-8')
                df = pd.read_csv(csv_file)

                # Iterate over the rows and insert into the database
                for _, row in df.iterrows():
                    participant = Participant(
                        username=row['username'],
                        email=row['email'],
                        batch_no=row['batch_no'],
                        linkedin_url=row.get('linkedin_url', None)
                    )
                    db.session.add(participant)

                db.session.commit()

                # Fetch all data from the Participant table
                participants = Participant.query.all()

                # Convert data to a list of dictionaries
                participants_data = [
                    {'username': participant.username, 'email': participant.email, 'batch_no': participant.batch_no, 'linkedin_url': participant.linkedin_url}
                    for participant in participants
                ]

                return render_template('show_user.html', participants_data=participants_data)

            else:
                return render_template('upload_csv.html', error='Invalid file format. Please upload a CSV file.', filename=None)

        except Exception as error:
            return render_template('upload_csv.html', error='Error processing the file.', filename=None)

    return render_template('upload_csv.html', filename=None)


def index_controller():
    try:
        # Fetch all data from the Participant table
        participants = Participant.query.all()
        print(participants, 'participants')
        if participants:
            # Convert data to a list of dictionaries
            participants_data = [
                {'username': participant.username, 
                 'email': participant.email, 
                 'batch_no': participant.batch_no, 
                 'linkedin_url': participant.linkedin_url}
                for participant in participants
            ]
        else:
            print('i am indide')
            participants_data = None
        return render_template('show_user.html', participants_data=participants_data)
    except Exception as error:
        print('helloe' , str(error))
        return render_template('500.html')

    
def view_user_controller():
    try:
        # Fetch all data from the Participant table
        participants = Participant.query.all()
        if any(participants):
            # Convert data to a list of dictionaries
            participants_data = [
                {'username': participant.username, 
                 'email': participant.email, 
                 'batch_no': participant.batch_no, 
                 'linkedin_url': participant.linkedin_url}
                for participant in participants
            ]
        else:
            participants_data = None
        return render_template('show_user.html', participants_data=participants_data)
    except Exception as error:
        return render_template('500.html')
    

def play_view_controller():
    try:
        if request.method == "GET":
            random_participant_dict = {
                    'username': None,
                    'linkedin_url': None,
                    'batch_no': None
                }
        if request.method == 'POST':
            # If the form is submitted, fetch a new random participant
            random_participant = Participant.query.order_by(func.random()).first()
            if random_participant == None:
                random_participant_dict =  None
            else:
                print('i have data')
                random_participant_dict = {
                    'username': random_participant.username,
                    'linkedin_url': random_participant.linkedin_url,
                    'batch_no': random_participant.batch_no
                }
        return render_template('play.html', random_participant=random_participant_dict)
    except Exception as error:
        return render_template('500.html')
    


def empty_user_controller():
    try:
        if db.session.query(Participant).count() > 0:
            # Perform a bulk delete operation
            db.session.query(Participant).delete()

            # Commit the changes to the database
            db.session.commit()
        return render_template('upload_csv.html')
    except Exception as error:
        return render_template('500.html')