from app import app
from flask import render_template
from app.user.login import is_logged_in


@app.route('/profile')
@is_logged_in
def profile():
    # TODO link with db
        # cur = mysql.connection.cursor()
        # result = cur.execute("SELECT * from profiles where UserId = %d", session["UserId"])
        # profile = cur.fetchone()
        # print("PRODUCT = ",profile)

        profile = {"name": "BMW", "photo": "https://www.bmw-m.com/content/dam/bmw/marketBMW_M/common/topics/magazine-article-pool/2019/bmw-m-wallpaper/bmw-m850i-individual-night-sky-gallery-01.jpg",
                   "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vel nulla sed magna pellentesque elementum. Duis malesuada sapien et neque imperdiet fringilla. Vivamus ac cursus dui."}
        return render_template('profile.html', profile=profile)

