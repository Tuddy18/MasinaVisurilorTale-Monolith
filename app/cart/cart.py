from app import app
from flask import flash, redirect, url_for, session, render_template
from app.config import mysql
from app.user.login import is_logged_in


@app.route('/addToCart/<path:name>')
@is_logged_in
def addToCart(name):
    # cur = mysql.connection.cursor()
    # result = cur.execute("SELECT * FROM cart where user_id = {} and state = 'ACTIVE'".format(session['userId']))
    # if result == 0:
    #     cur.execute("INSERT INTO cart(user_id, total_price, state) VALUES ({}, 0, 'ACTIVE')".format(session['userId']))
    # cur.execute("SELECT * FROM cart where user_id = {} and state = 'ACTIVE'".format(session['userId']))
    # data = cur.fetchone()
    # cur.execute("INSERT INTO cart_items(cart_id, product_id, quantity) VALUES ({0}, {1}, {2})".format(data['cart_id'], id, 1))
    # cur.execute("UPDATE cart,product SET cart.total_price=cart.total_price+product.price WHERE product.product_id={}".format(id))
    # mysql.connection.commit()
    # cur.close()
    flash('You have successfully selected ' + name + ' profile', 'success')
    return redirect(url_for('index'))


@app.route('/cart')
@is_logged_in
def cart():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * from product WHERE product_id=1")
    recommandations = cur.fetchall()
    if result > 0:
        return render_template('cart.html', recommandations=recommandations)
    else:
        return render_template('cartEmpty.html')
