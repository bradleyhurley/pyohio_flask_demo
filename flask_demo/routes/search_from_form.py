import flask
from flask_demo.forms import SearchForm
from flask_demo.services.search import search_service

blueprint = flask.Blueprint('search_from_form', __name__)


@blueprint.route('/search_v4',  methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if flask.request.method == 'POST':
        if not form.validate():
            flask.flash("Invalid Search String", 'danger')
            return flask.render_template('search.html', form=form)
        search_value = flask.request.form['search_value']
        results = search_service(search_value)
        return flask.render_template('search_results.html', results=results, version=4)

    else:
        return flask.render_template('search.html', form=form)
