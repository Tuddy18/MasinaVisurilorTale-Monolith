from app import app
from flask import flash, redirect, url_for, session, render_template
from app.config import mysql
from app.user.login import is_logged_in


@app.route('/addToCart/<path:name>')
@is_logged_in
def addToCart(name):
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
    flash('You have successfully selected ' + name + ' profile', 'success')
    return redirect(url_for('index'))


@app.route('/match')
@is_logged_in
def cart():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * from product WHERE product_id=1")
    recommandations = cur.fetchall()
    if result > 0:
        return render_template('match.html', recommandations=recommandations)
    else:
        return render_template('matchEmpty.html')
