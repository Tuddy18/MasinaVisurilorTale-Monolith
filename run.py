#!flask/bin/python
from app import app

app.secret_key='secret'
if __name__ == '__main__':
    app.run()
