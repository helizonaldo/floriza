from flask import Flask, render_template

from app.settings import config_object
from app import home

def create_app(config_object=config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)   

    register_errorhandlers(app)
    register_blueprints(app)

    return app



def register_blueprints(app):
    app.register_blueprint(home.views.blueprint)    

    return None


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code
    # 400 - Bad Request
    # 403 - Forbidden
    # 404 - Page Not Found
    # 405 - Method Not Allowed
    # 500 - Internal Server Error
    for errcode in [400,403, 404, 405, 500]:
        app.register_error_handler(errcode, render_error)

    return None
