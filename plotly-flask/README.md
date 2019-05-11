# plotly-flask: using plotly.offline with python flask

**plotly-flask** is a demo app showing how the [Plotly] plotting library may be combined with the Python [Flask] framework to serve up an interactive plot. The plot is taken from Plotly's [3D Scatter plot](https://plot.ly/python/3d-scatter-plots/).

## Host Machine Prereqs

* [Make]
* [Docker]
* [docker-compose]

## Running the Docker Container

The Makefile provides a convenient wrapper for several docker-compose commands:

| Command       | Purpose                                          |
|---------------|--------------------------------------------------|
| `make build`  | Build docker image                               |
| `make up`     | Run a container in the foreground to stream logs |
| `make server` | Run a container in the background                |
| `make shell`  | Open a bash shell on running container           |
| `make down`   | Stop and remove running container                |

Run `make build` to build the Flask app's Docker image. Start the container with `make up` (if you want to stream the logs) or `make server` (no logs streamed).

The container runs a [gunicorn] WSGI server to serve up the Flask app (versus directly running Flask's development server, which is unsuited for production use).

The docker-compose.yaml file maps the container port 5000 out to host machine port number 5001. To reach the running app, open http://localhost:5001/ in your browser.

Optionally do `make shell` if you need to work inside the container. Stop and remove the running container with `make down`.

## Example Usage

```bash
$ cd plotly-flask
$ ls
Makefile            README.md           app                 docker-compose.yaml
$
$ # build the Docker image
$ make build
------------------
- Building image -
------------------
docker-compose build && docker image prune -f
Building app
Step 1/8 : FROM python:3.7-slim
 . . .
Successfully built d6549f75ae2b
Successfully tagged plotly-flask_app:latest
$
$ # run a container in the background
$ make server && docker ps -a
----------------------------------------
- Starting app container in background -
----------------------------------------
docker-compose up -d
Recreating plotly-flask ... done
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                    NAMES
bb126d4a3156        plotly-flask_app    "gunicorn -c conf/gu…"   2 seconds ago       Up Less than a second   0.0.0.0:5001->5000/tcp   plotly-flask
```

Then open http://localhost:5001/ in your browser to reach the running app. To stop the app:
```bash
$ make down && docker ps -a
-------------------------------------
- Stop and Remove running container -
-------------------------------------
docker-compose down
Stopping plotly-flask ... done
Removing plotly-flask ... done
Removing network plotly-flask_default
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
$
```

<!-- Links -->
[Docker]: https://www.docker.com/community-edition#/download
[docker-compose]: https://docs.docker.com/compose/install/
[Flask]: http://flask.pocoo.org/
[gunicorn]: http://docs.gunicorn.org/en/stable/
[Make]: http://man7.org/linux/man-pages/man1/make.1.html
[Plotly]: https://plot.ly/python/offline/
