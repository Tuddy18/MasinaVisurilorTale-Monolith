from app import app
from app.config import mysql
from flask import request, render_template, flash, redirect, url_for, session
from flask import render_template
from app.user.login import is_logged_in


@app.route('/')
@is_logged_in
def profile():
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * from product")
        products = cur.fetchall()
        print("PRODUCT = ",products)
        return render_template('index.html', products=products)
