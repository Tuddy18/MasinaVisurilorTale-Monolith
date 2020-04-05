from app import app
from flask import render_template
from app.config import mysql
from flask import request, render_template, flash, redirect, url_for, session, jsonify
from app.user.login import is_logged_in


@app.route('/profile')
@is_logged_in
def profile():
    # TODO link with db
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * from Profile where AccountId = %s", [str(session["accountId"])])
        profile = cur.fetchone()
        print("Profile = ",profile)
        session["ProfileId"] = profile["ProfileId"]

        cur.execute("SELECT Url from Photo where ProfileId = %s", [str(profile["ProfileId"])])
        # save photos as tuple of index and url, so we can access for loop index
        profile_photos = [(i, el['Url']) for (i, el) in enumerate(cur.fetchall())]

        if len(profile_photos) == 0:
            profile_photos.append((0, "https://cdn.iconscout.com/icon/free/png-256/car-disconnected-lost-connection-laptop-device-29510.png"))
        cur.execute("SELECT * from Features where ProfileId = %s", [str(profile["ProfileId"])])
        features = [el["FeatureText"] for el in cur.fetchall()]


        cur.execute("SELECT * from Preferences where ProfileId = %s", [str(profile["ProfileId"])])
        preferences = [el["PreferenceText"] for el in cur.fetchall()]


        profile = {"name": profile["Name"], "photo": profile_photos[0][1], "profile_type": profile["ProfileType"],
                   "description": profile["Description"]}
        return render_template('profile.html', profile=profile, profile_photos=profile_photos, features=features, preferences=preferences)

