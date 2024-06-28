from flask import Blueprint, render_template, flash, request, redirect, url_for
from models import Note, db
from flask_login import login_required, current_user

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        note_text = request.form.get('note')

        if len(title) == 0:
            flash('Title cannot be empty!', category='error')
        elif len(note_text.strip()) <= 0:
            flash('Note cannot be empty!', category='error')
        else:
            # Create a new note object
            new_note = Note(title=title, note=note_text,
                            user_id=current_user.id)

            # Add the note to the database session
            db.session.add(new_note)

            # Commit the changes to the database
            db.session.commit()

            flash('Note created successfully', category='success')
            # Redirect to the dashboard
            return redirect(url_for('index.home'))

    # Render the template for adding a note
    return render_template('home.html', user=current_user)
