from flask import Flask
from config import config
from routes import user

app = Flask(__name__)

def pageNotFound(error):
    return "Page not found", 404

if __name__ ==  "__main__":
    app.config.from_object(config["config"])
    app.register_blueprint(user.main, url_prefix='/users/')
    app.register_error_handler(404, pageNotFound)
    app.run()