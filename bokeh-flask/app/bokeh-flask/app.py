"""
The Flask app (to be served by gunicorn)
"""
import os
from flask import Flask, render_template
import bokeh
import plotter

app = Flask(__name__)


@app.route("/")
def index():
    """Route which renders a bokeh plot"""

    # retrieve a bokeh.plotting.figure object from plotter module
    plot = plotter.generate_plot()

    # pass that object to bokeh.embed.components, which returns two strings:
    #   script == '<script> . . . </script>'
    #   div == '<div> . . . </div>'
    script, div = bokeh.embed.components(plot)

    # pass those two strings into the Jinja2 template
    return render_template("index.html", script=script, div=div)


if __name__ == "__main__":
    debug = os.environ.get('FLASK_DEBUG', False)
    app.run(host='0.0.0.0', debug=debug)
