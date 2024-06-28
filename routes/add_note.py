from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import Note, db

# Define the addNote blueprint
addNote = Blueprint('addNote', __name__)


# Created the addNote route
@addNote.route('/add_note', methods=['GET', 'POST'])
@login_required
def add_note():
    # Conditional statement to handle the post request when a note is submitted
    if request.method == 'POST':
        title = request.form.get('title')
        note_text = request.form.get('note')

        # conditional statement to validate the note
        if len(title) > 15:
            flash('Length of title too long! Try something shorter', category='error')
        elif len(title) == 0:
            flash('Title cannot be empty!', category='error')
        elif len(note_text) == 0:
            flash('Note cannot be empty!', category='error')
        else:
            # Create a new note object
            new_note = Note(title=title, note=note_text, user=current_user)

            # Add the note to the database session
            db.session.add(new_note)

            # Commit the changes to the database
            db.session.commit()

            # flash the success message to the browser
            flash('Note created successfully', category='success')
            # redirect the user to dashboard
            return redirect(url_for('dashboard'))

    # Render the template for adding a note
    return render_template('add_note.html')
