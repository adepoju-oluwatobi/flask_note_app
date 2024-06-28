from flask import request, Blueprint, render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from models import User, db

# Create a Blueprint for authentication routes
auth = Blueprint('auth', __name__, 'auth')

# Route for user login


@auth.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if len(email) <= 0:
            flash('Email field is required!', category='error')
        elif len(password) <= 0:
            flash('Password field is required', category='error')
        else:
            # Query the database to find the user by email
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                # Login successful
                flash('Login Successful!', category='success')
                login_user(user, remember=True)  # Log in the user
                # Redirect to the home page
                return redirect(url_for('index.home'))
            else:
                flash('Invalid email or password!', category='error')
    return render_template('login.html', user=current_user)

# Route for user signup


@auth.route('/user_signup', methods=['GET', 'POST'])
def user_signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check if the user already exists in the database
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters!', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character!', category='error')
        elif password1 != password2:
            flash('Passwords do not match please check again!', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than 7 characters!', category='error')
        else:
            try:
                # Hash the password
                hashed_password = generate_password_hash(password1)
                # Add user to the database with hashed password
                new_user = User(email=email, name=name,
                                password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Account Created!', category='success')
                # Redirect to login page after successful signup
                return redirect(url_for('auth.user_login'))
            except IntegrityError:
                # Rollback changes if there's an integrity error (e.g., duplicate email)
                db.session.rollback()
                flash('Error creating account. Please try again.', category='error')

    return render_template('signUp.html', user=current_user)


# Route for user logout
@auth.route('/logout')
@login_required
def logout():
    # Log out the user
    logout_user()
    # Redirect to the login page
    return redirect(url_for('auth.user_login'))
