from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error


# def create_app(config_name):
#     app = Flask(__name__)


#     app.config.from_object(config_options[config_name])

#     bootstrap.init_app(app)


#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)


#     from .requests import configure_request
#     configure_request(app)
#     return app

