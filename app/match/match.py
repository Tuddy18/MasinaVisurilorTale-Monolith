from app import app
from flask import flash, redirect, url_for, session, render_template, request
from app.config import mysql
from app.user.login import is_logged_in
from datetime import datetime


# @app.route('/addToCart/<path:name>')
# @is_logged_in
# def addToCart(name):
# cur = mysql.connection.cursor()
# result = cur.execute("SELECT * FROM match where user_id = {} and state = 'ACTIVE'".format(session['userId']))
# if result == 0:
#     cur.execute("INSERT INTO match(user_id, total_price, state) VALUES ({}, 0, 'ACTIVE')".format(session['userId']))
# cur.execute("SELECT * FROM match where user_id = {} and state = 'ACTIVE'".format(session['userId']))
# data = cur.fetchone()
# cur.execute("INSERT INTO cart_items(cart_id, product_id, quantity) VALUES ({0}, {1}, {2})".format(data['cart_id'], id, 1))
# cur.execute("UPDATE match,product SET match.total_price=match.total_price+product.price WHERE product.product_id={}".format(id))
# mysql.connection.commit()
# cur.close()
# flash('You have successfully selected ' + name + ' profile', 'success')
# return redirect(url_for('index'))


@app.route('/match', methods=['POST'])
@is_logged_in
def match():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from Profile where AccountId = %s", str(session["accountId"]))
    profile = cur.fetchone()
    cur.execute("SELECT * FROM photo WHERE photo.ProfileId != {0} AND photo.ProfileId NOT IN "
                "(SELECT matchedcontact.FirstProfileId "
                "FROM matchedcontact "
                "WHERE matchedcontact.SecondProfileId = {0} AND matchedcontact.SecondProfileLike = {0} "
                "UNION SELECT matchedcontact.SecondProfileId "
                "FROM matchedcontact "
                "WHERE matchedcontact.FirstProfileId = {0} AND matchedcontact.FirstProfileLike = {0}); "
                "LIMIT 1;"
                .format(str(profile["ProfileId"])))
    recommendations = cur.fetchall()
    if recommendations == 0:
        flash('There are no recommendations for you at the moment')
    else:
        return render_template('match.html', recommendations=recommendations)

    liked = False
    profile_id = str(profile["ProfileId"])
    likedProfile_id = recommendations[0].ProfileId

    if request.method == 'POST':
        if request.form['submit_button'] == 'Like':
            liked = True
        elif request.form['submit_button'] == 'Dislike':
            liked = False
        cur.execute("SELECT * FROM MatchedContact "
                    "WHERE MatchedContact.FirstProfileId = {0}} "
                    "AND MatchedContact.SecondProfileId = {1}}"
                    .format(profile_id, likedProfile_id))
        mysql.connection.commit()
        if cur.fetchall() != 0:
            cur.execute("UPDATE TABLE MatchedContact "
                        "SET MatchedContact.FirstProfileLike = {0}, MatchedContact.MatchedDateTime = {1} "
                        "WHERE MatchedContact.FirstProfileId = {2} "
                        "AND MatchedContact.SecondProfileId = {3};"
                        .format(liked, datetime.now(), profile_id, likedProfile_id))
            mysql.connection.commit()
        else:
            cur.execute("SELECT * FROM MatchedContact "
                        "WHERE FirstProfileId = {0} AND SecondProfileId = {1};"
                        .format(likedProfile_id, profile_id))
            mysql.connection.commit()
            if cur.fetchall() != 0:
                cur.execute("UPDATE TABLE MatchedContact "
                            "SET FirstProfileLike = {0}, MatchedDateTime = {1} "
                            "WHERE FirstProfileId = {2} AND SecondProfileId = {3};"
                            .format(liked, datetime.now(), likedProfile_id, profile_id))
                mysql.connection.commit()
            else:
                cur.execute("INSERT INTO MatchedContact(FirstProfileId, SecondProfileId"
                            ", FirstProfileLike, FirstProfileLike, MatchedDateTime) "
                            "VALUES({0}, {1}, {2}, {3});"
                            .format(profile_id, likedProfile_id, liked, datetime.now()))
                mysql.connection.commit()

    #cur.fetchall()
    # recommandations = cur.fetchall()
    # if result > 0:
    #   return render_template('match.html', recommandations=recommandations)
    # else:
    #   return render_template('matchEmpty.html')

    mysql.connection.commit()
    cur.close()
    return redirect(url_for('match'))
