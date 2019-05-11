"""
This module is imported by app.py.
"""
import numpy as np
import plotly.graph_objs as go


def plot_3d_scatter():
    """
    Returns a plotly graph objects Figure, adapted from the example shown in
    https://plot.ly/python/3d-scatter-plots/
    """

    x, y, z = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 50).transpose()
    trace1 = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=5,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=0.8
        )
    )

    x2, y2, z2 = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 50).transpose()
    trace2 = go.Scatter3d(
        x=x2,
        y=y2,
        z=z2,
        mode='markers',
        marker=dict(
            color='rgb(127, 127, 127)',
            size=5,
            symbol='circle',
            line=dict(
                color='rgb(204, 204, 204)',
                width=1
            ),
            opacity=0.9
        )
    )
    data = [trace1, trace2]
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        ),
        legend=dict(orientation='h')
    )

    return go.Figure(data=data, layout=layout)
