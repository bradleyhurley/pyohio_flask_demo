import requests
import json
from flask_demo.constants import API_KEY, CX_ID


def search_service(query="Flask"):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': CX_ID,
        'q': query
    }
    r = requests.get(search_url, params=params)
    response = r.content.decode('utf-8')
    result = json.loads(response)
    return result['items']
