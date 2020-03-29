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
        # svae photos as tuple of index and url, so we can access for loop index
        profile_photos = [(i, el['Url']) for (i, el) in enumerate(cur.fetchall())]

        profile = {"name": profile["Name"], "photo": profile_photos[0][1],
                   "description": profile["Description"]}
        return render_template('profile.html', profile=profile, profile_photos=profile_photos)

