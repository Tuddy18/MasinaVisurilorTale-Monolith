from app import app
from flask import flash, redirect, url_for, session, render_template, jsonify, request
from app.config import mysql
from app.user.login import is_logged_in
from datetime import datetime


@app.route('/match/add',  methods=['POST'])
@is_logged_in
def match_add():
    cur = mysql.connection.cursor()

    liked_profile_id = request.form["profile_id"]
    liked = request.form["liked"]
    now = datetime.now()
    now = now.strftime('%Y:%m:%d %H:%M:%S')

    cur.execute("SELECT * from Profile where AccountId = %s", [str(session["accountId"])])
    profile = cur.fetchone()
    profile_id = str(profile["ProfileId"])

    result = cur.execute("SELECT * FROM MatchedContact WHERE MatchedContact.FirstProfileId = {0} "
                         "AND MatchedContact.SecondProfileId = {1}"
                         .format(profile_id, liked_profile_id))

    if result > 0:
        cur.execute("UPDATE MatchedContact "
                    "SET MatchedContact.FirstProfileLike = {0}, MatchedContact.MatchDateTime = \'{1}\' "
                    "WHERE MatchedContact.FirstProfileId = {2} "
                    "AND MatchedContact.SecondProfileId = {3};"
                    .format(liked,  now, profile_id, liked_profile_id))
    else:
        result = cur.execute("SELECT * FROM MatchedContact WHERE FirstProfileId = {0} AND SecondProfileId = {1};"
                             .format(liked_profile_id, profile_id))
        if result > 0:
            cur.execute("UPDATE MatchedContact "
                        "SET SecondProfileLike = {0}, MatchDateTime = \'{1}\' "
                        "WHERE FirstProfileId = {2} AND SecondProfileId = {3};"
                        .format(liked, now, liked_profile_id, profile_id))
        else:
            cur.execute("INSERT INTO MatchedContact(FirstProfileId, SecondProfileId"
                        ", FirstProfileLike, MatchDateTime) "
                        "VALUES({0}, {1}, {2}, \'{3}\');"
                        .format(profile_id, liked_profile_id, liked, now))
    mysql.connection.commit()
    cur.close()
    resp = jsonify(success=True)
    return resp


@app.route('/match')
@is_logged_in
def match():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from Profile where AccountId = %s", [str(session["accountId"])])
    profile = cur.fetchone()
    result = cur.execute("SELECT Photo.ProfileId FROM Photo "
                         "INNER JOIN (SELECT Photo.ProfileId FROM Photo "
                         "WHERE Photo.ProfileId != {0} AND Photo.ProfileId NOT IN ("
                         "SELECT MatchedContact.FirstProfileId FROM MatchedContact "
                         "WHERE MatchedContact.SecondProfileId = {0} "
                         "AND (MatchedContact.SecondProfileLike = 1 OR MatchedContact.SecondProfileLike = 0) "
                         "UNION "
                         "SELECT MatchedContact.SecondProfileId FROM MatchedContact "
                         "WHERE MatchedContact.FirstProfileId = {0} "
                         "AND (MatchedContact.FirstProfileLike = 1 OR MatchedContact.FirstProfileLike = 0)) ) "
                         "t ON Photo.ProfileId = t.ProfileId "
                         "INNER JOIN (SELECT Profile.ProfileId FROM Profile "
                         "WHERE ProfileType NOT IN (SELECT ProfileType FROM Profile WHERE ProfileId = {0})) p "
                         "ON Photo.ProfileId = p.ProfileId"
                         .format(str(profile["ProfileId"])))

    if result > 0:
        match_id = cur.fetchall()[0]['ProfileId']
        cur.execute("SELECT * FROM Photo "
                    "INNER JOIN (SELECT * FROM Profile) p "
                    "ON Photo.ProfileId = p.ProfileId WHERE Photo.ProfileId = {0}".format(match_id))
        recommendations = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('match.html', recommendations=recommendations)
    else:
        cur.close()
        return render_template('matchEmpty.html')
