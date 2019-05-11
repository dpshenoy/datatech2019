# bokeh-flask: using bokeh.embed.components with python flask

**bokeh-flask** is a demo app showing how the [Bokeh] plotting library may be combined with the Python [Flask] framework to serve up an interactive plot. The data displayed are Bokeh's [demo scatterplot of the iris data set](https://bokeh.pydata.org/en/latest/docs/gallery/iris.html#iris-py), taken from the project's gallery of [standalone demos](https://bokeh.pydata.org/en/latest/docs/gallery.html#standalone-examples).

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

The docker-compose.yaml file maps the container port 5000 out to the same host machine port number. To reach the running app, open http://localhost:5000/ in your browser.

Optionally do `make shell` if you need to work inside the container. Stop and remove the running container with `make down`.

## Example Usage

```bash
$ cd bokeh-flask
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
Successfully built 1610ef041d78
Successfully tagged bokeh-flask_app:latest
$
$ # run a container in the background
$ make server && docker ps -a
----------------------------------------
- Starting app container in background -
----------------------------------------
docker-compose up -d
Creating network "bokeh-flask_default" with the default driver
Creating bokeh-flask ... done
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                    NAMES
58cf6ea8cb2c        bokeh-flask_app     "gunicorn -c conf/gu…"   2 seconds ago       Up Less than a second   0.0.0.0:5000->5000/tcp   bokeh-flask
$
```

Then open http://localhost:5000 in your browser to reach the running app. To stop the app:
```bash
$ make down && docker ps -a
-------------------------------------
- Stop and Remove running container -
-------------------------------------
docker-compose down
Stopping bokeh-flask ... done
Removing bokeh-flask ... done
Removing network bokeh-flask_default
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
$
```

<!-- Links -->
[Bokeh]: https://bokeh.pydata.org/en/latest/
[Docker]: https://www.docker.com/community-edition#/download
[docker-compose]: https://docs.docker.com/compose/install/
[Flask]: http://flask.pocoo.org/
[gunicorn]: http://docs.gunicorn.org/en/stable/
[Make]: http://man7.org/linux/man-pages/man1/make.1.html
