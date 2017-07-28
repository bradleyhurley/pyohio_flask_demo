import flask
from flask_demo.services import cache_demo_service

blueprint = flask.Blueprint('cache', __name__)


@blueprint.route('/cache')
def cache_demo():
    cache_demo_service.cache_demo()
    return "Was that 10 seconds?"
