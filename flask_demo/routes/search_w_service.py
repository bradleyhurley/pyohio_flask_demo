import flask
from flask_demo.services.search import search_service

blueprint = flask.Blueprint('search_w_service', __name__)


@blueprint.route('/search_v3')
def search():
    results = search_service()
    return flask.render_template('search_results.html', results=results, version=3)
