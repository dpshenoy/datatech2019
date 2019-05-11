# datatech2019

This repo contains demo web apps for my 2019 May 30 presentation **[Do It Yourself Interactive Data Visualization: Starting Simple (And Keeping It That Way)](https://datatech2019.sched.com/event/PDMb/do-it-yourself-interactive-data-visualization-starting-simple-and-keeping-it-that-way)** at the [Minneanalytics' DataTech 2019](http://minneanalytics.org/datatech/) conference in Bloomington, MN.

There are two demo web apps:

* [bokeh-flask](./bokeh-flask/README.md) -- a Python Flask app serving an interactive plot made using the [Bokeh](https://bokeh.pydata.org) library.


* [plotly-flask](./plotly-flask/README.md) -- a Python Flask app serving an interactive plot made using the [Plotly](https://plot.ly/python/) library.


In each app's subdirectory the README provides more detail on how to run the app. Each app is containerized because:

* it eases local development by ensuring all properly-versioned pip packages are available to the app; and
* it makes the app automatically ready for deployment to a production environment such as Kubernetes.

The Makefile in each subdirectory provides a convenient wrapper for docker-compose commands, which are themselves are a layer of convenience above the actual docker commands to build the image and to start/stop a container from the image.

If you are not familiar with Docker, please feel free to check out my [docker-basics](https://github.com/dpshenoy/docker-basics) repo, which also contains several examples you can try out for yourself.

**Note:** These apps have been purposely kept as simple as possible. The focus of this presentation is on how to get the benefits of interactive data visualization in a Python web app without needing to know much JavaScript. Additions suitable to a production-worthy app (getting live data from another source; caching the data; providing options for filtering the data; setting filters' content as the values of query string params for bookmarkable URLs, etc.) have been omitted.