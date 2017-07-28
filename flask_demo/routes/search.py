import json
import requests
import flask
from flask_demo.constants import API_KEY, CX_ID

blueprint = flask.Blueprint('search', __name__)


@blueprint.route('/search')
def search():
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': CX_ID,
        'q': 'flask'
    }
    r = requests.get(search_url, params=params)
    response = r.content.decode('utf-8')
    result = json.loads(response)

    return result['items'][1]['formattedUrl']


@blueprint.route('/search_v2')
def search_v2():
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': CX_ID,
        'q': 'flask'
    }
    r = requests.get(search_url, params=params)
    response = r.content.decode('utf-8')
    result = json.loads(response)
    return flask.render_template('search_results.html', results=result['items'], version=2)
