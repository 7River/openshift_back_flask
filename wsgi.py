from flask import Flask
from flask_cors import CORS
application = Flask(__name__)
CORS(application)
# CORS(application,resources={r"/*": {"origins": "*"}}

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
