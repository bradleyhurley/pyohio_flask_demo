import flask

blueprint = flask.Blueprint('views', __name__)


@blueprint.route('/')
def index():
    return flask.render_template('index.html')
