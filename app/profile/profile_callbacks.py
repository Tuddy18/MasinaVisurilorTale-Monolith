from app import app
from flask import render_template
from app.config import mysql
from flask import request, render_template, flash, redirect, url_for, session, jsonify
from app.user.login import is_logged_in

@app.route('/profile/add-photo',  methods = ['POST'])
@is_logged_in
def profile_add_photo():
    photo_url = request.form["photo_url"]
    cur = mysql.connection.cursor()
    cur.execute("Insert into Photo(ProfileId, Url) Values(%s, %s)", (str(session["ProfileId"]), photo_url))
    mysql.connection.commit()
    resp = jsonify(success=True)
    return resp

@app.route('/profile/remove-photo',  methods = ['POST'])
@is_logged_in
def profile_remove_photo():
    photo_url = request.form["photo_url"]
    cur = mysql.connection.cursor()
    cur.execute("delete from Photo where ProfileId = %s and Url = %s", (str(session["ProfileId"]), photo_url))
    mysql.connection.commit()
    resp = jsonify(success=True)
    return resp

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