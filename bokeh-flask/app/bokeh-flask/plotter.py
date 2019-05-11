"""
This module is imported by app.py.
"""
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers


def generate_plot():
    """
    Returns a bokeh.plotting.figure, adapted from the example shown in
    https://bokeh.pydata.org/en/latest/docs/gallery/iris.html#iris-py
    A hover tool and zoom have been added to the example.
    """

    # bokeh.sampledata.iris.flowers is a pandas DataFrame; add a color column
    colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    flowers['colors'] = flowers['species'].apply(lambda x: colormap[x])

    source = ColumnDataSource(flowers)

    hover = HoverTool(tooltips=[
        ("petal_width", "@petal_width"),
        ("petal_length", "@petal_length"),
        ("species", "@species")
    ])

    tools = [hover, 'pan,box_zoom,wheel_zoom,reset']

    p = figure(
        title="Iris Data Set: Petal Width vs Length", tools=tools,
        active_drag='box_zoom', width=1400, height=700
    )

    p.circle(
        source=source, x='petal_width', y='petal_length', color='colors',
        fill_alpha=0.2, size=10
    )

    p.title.text_font_size = '16pt'
    p.xaxis.axis_label = 'Petal Width'
    p.yaxis.axis_label = 'Petal Length'
    p.axis.axis_label_text_font_style = 'normal'
    p.axis.axis_label_text_font_size = '14pt'
    p.axis.major_label_text_font_size = '12pt'
    p.axis.axis_label_standoff = 15

    return p
