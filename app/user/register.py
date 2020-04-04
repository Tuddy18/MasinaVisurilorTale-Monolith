from app import app
from app.forms.register import RegisterForm
from flask import request, render_template, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from app.config import mysql

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        name = form.name.data
        profileType = form.profileType.data
        description = form.description.data

        # Create cursor
        cur = mysql.connection.cursor()

        if cur.execute("SELECT * FROM Account WHERE Username = %s", [username]) > 0:
            return render_template('register.html', form=form)

        cur.execute("INSERT INTO Account(Username, Password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()

        cur.execute("SELECT AccountId FROM Account WHERE Username = %s", [username])
        account_id = cur.fetchall()[0]

        cur.execute("INSERT INTO Profile(AccountId, Name, ProfileType, Description) VALUES (%s, %s, %s, %s)",
                    (account_id['AccountId'], name, profileType, description))


        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can login', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)
