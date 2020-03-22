from app import app
from flask import render_template
from app.config import mysql
from flask import request, render_template, flash, redirect, url_for, session
from app.user.login import is_logged_in


@app.route('/profile')
@is_logged_in
def profile():
    # TODO link with db
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * from Profile where AccountId = %s", str(session["accountId"]))
        profile = cur.fetchone()
        print("PRODUCT = ",profile)

        cur.execute("SELECT Url from Photo where ProfileId = %s", str(profile["ProfileId"]))
        profile_photo = cur.fetchone()['Url']

        profile = {"name": profile["Name"], "photo": profile_photo,
                   "description": profile["Description"]}
        return render_template('profile.html', profile=profile)

