FROM python:3.7-slim

RUN set -x \
    && apt-get -qq update \
    && apt-get install -yq --no-install-recommends procps vim \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
ADD requirements.txt /app/requirements.txt
RUN pip install pip --upgrade \
    && pip install -r /app/requirements.txt

ADD ./plotly-flask /app/plotly-flask
WORKDIR /app/plotly-flask
USER nobody
