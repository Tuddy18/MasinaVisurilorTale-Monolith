from app import app
from flask_mysqldb import MySQL
import os

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'eYHL3f9DbJ'
app.config['MYSQL_PASSWORD'] = 'nWp7J02COR'
app.config['MYSQL_DB'] = 'eYHL3f9DbJ'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'masina_visurilor_tale'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# app.config['MYSQL_HOST'] = os.environ['MYSQL_DB_HOST']
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_DB_PASSWORD']
# app.config['MYSQL_DB'] = 'ecommerce'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

