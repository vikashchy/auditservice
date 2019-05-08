from flask import Flask
import constants
import dbhelper

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True,host=constants.HOST,port=constants.PORT)

