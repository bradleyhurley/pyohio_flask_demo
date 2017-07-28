from flask import Flask
from flask_demo.config import config
from flask_demo.extensions import bootstrap
from flask_demo.extensions import cache


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # this is needed to prevent circular imports
    register_blueprints(app)
    register_extensions(app)

    cache.init_app(app, config)

    app.logger.info('Application startup')
    return app


def register_blueprints(app):
    from flask_demo.routes.search import blueprint as search_blueprint
    from flask_demo.routes.search_w_service import blueprint as service_search_blueprint
    from flask_demo.routes.search_from_form import blueprint as form_search_blueprint
    from flask_demo.routes.views import blueprint as view_blueprint
    from flask_demo.routes.cache_demo import blueprint as cache_blueprint

    default_blueprints = (search_blueprint,
                          view_blueprint,
                          service_search_blueprint,
                          form_search_blueprint,
                          cache_blueprint)

    for blueprint in default_blueprints:
        app.register_blueprint(blueprint)


def register_extensions(app):
    bootstrap.init_app(app)
