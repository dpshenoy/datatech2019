"""
The Flask app (to be served by gunicorn)
"""
import os
from flask import Flask, render_template
import plotly
import plotter

app = Flask(__name__)


@app.route("/")
def index():
    """Route which renders a plotly.offline.plot"""

    # retrieve a plotly graph objects Figure
    fig = plotter.plot_3d_scatter()

    # pass the Figure to plotly.offline.plot with output_type='div',
    # which returns a string for a <div> that includes a <script> tag
    # holding the minified JavaScript
    div = plotly.offline.plot(fig, output_type='div')

    # pass the string into the Jinja2 template
    return render_template("index.html", div=div)


if __name__ == "__main__":
    debug = os.environ.get('FLASK_DEBUG', False)
    app.run(host='0.0.0.0', debug=debug)
