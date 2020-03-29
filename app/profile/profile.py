from app import app
from flask import render_template
from app.config import mysql
from flask import request, render_template, flash, redirect, url_for, session, jsonify
from app.user.login import is_logged_in


@app.route('/profile/add-feature',  methods = ['POST'])
@is_logged_in
def profile_add_feature():
    feature_text = request.form["feature_text"]
    cur = mysql.connection.cursor()
    cur.execute("Insert into Features(ProfileId, FeatureText) Values(%s, %s)", (str(session["ProfileId"]), feature_text))
    mysql.connection.commit()
    resp = jsonify(success=True)
    return resp

@app.route('/profile/remove-feature',  methods = ['POST'])
@is_logged_in
def profile_remove_feature():
    feature_text = request.form["feature_text"]
    cur = mysql.connection.cursor()
    cur.execute("Delete from Features where ProfileId = %s and FeatureText = %s", (str(session["ProfileId"]), feature_text))
    mysql.connection.commit()
    resp = jsonify(success=True)
    return resp

@app.route('/profile/add-preference',  methods = ['POST'])
@is_logged_in
def profile_add_preference():
    preference_text = request.form["preference_text"]
    cur = mysql.connection.cursor()
    cur.execute("Insert into Preferences(ProfileId, PreferenceText) Values(%s, %s)", (str(session["ProfileId"]), preference_text))
    mysql.connection.commit()
    resp = jsonify(success=True)
    return resp

@app.route('/profile/remove-preference',  methods = ['POST'])
@is_logged_in
def profile_remove_preference():
    preference_text = request.form["preference_text"]
    cur = mysql.connection.cursor()
    cur.execute("Delete from Preferences where ProfileId = %s and PreferenceText = %s", (str(session["ProfileId"]), preference_text))
    mysql.connection.commit()
    resp = jsonify(success=True)
    return resp

@app.route('/profile')
@is_logged_in
def profile():
    # TODO link with db
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * from Profile where AccountId = %s", str(session["accountId"]))
        profile = cur.fetchone()
        print("Profile = ",profile)
        session["ProfileId"] = profile["ProfileId"]

        cur.execute("SELECT Url from Photo where ProfileId = %s", str(profile["ProfileId"]))
        # save photos as tuple of index and url, so we can access for loop index
        profile_photos = [(i, el['Url']) for (i, el) in enumerate(cur.fetchall())]


        cur.execute("SELECT * from Features where ProfileId = %s", str(profile["ProfileId"]))
        features = [el["FeatureText"] for el in cur.fetchall()]


        cur.execute("SELECT * from Preferences where ProfileId = %s", str(profile["ProfileId"]))
        preferences = [el["PreferenceText"] for el in cur.fetchall()]

        profile = {"name": profile["Name"], "photo": profile_photos[0][1],
                   "description": profile["Description"]}
        return render_template('profile.html', profile=profile, profile_photos=profile_photos, features=features, preferences=preferences)

