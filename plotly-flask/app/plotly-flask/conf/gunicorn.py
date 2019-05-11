import os
from gunicorn.config import Config

c = Config()

#-------------------------
#- Runtime Configuration -
#-------------------------

#- socket to bind to (HOST, HOST:PORT, unix:PATH) -
bind = "{}:{}".format(
    os.environ.get('API_HOST', "0.0.0.0"),
    os.environ.get('API_PORT', 5000)
)

#- maximum number of pending connections -
backlog = os.environ.get('API_BACKLOG', c.backlog)

#- number of worker processes for handling requests -
workers = os.environ.get('API_WORKERS', 1)

#- maximum number of simultaneous clients -
worker_connections = os.environ.get('API_WORKER_CONNECTIONS', c.worker_connections)

#- maximum number of requests a worker will process before restarting -
max_requests = os.environ.get('API_MAX_REQUESTS', c.max_requests)

#- number of worker threads for handling requests (default: 1) -
threads = os.environ.get('API_THREADS', c.threads)

#- workers silent for more than this many seconds are killed and restarted -
timeout = os.environ.get('API_TIMEOUT', c.timeout)

#- The number of seconds to wait for requests on a Keep-Alive connection -
keepalive = os.environ.get('API_KEEPALIVE', c.keepalive)



#---------------------------
#- Debugging Configuration -
#---------------------------

#- restart workers when code changes -
reload = os.environ.get('API_RELOAD', False)

#- install a trace function that spews every line executed by the server -
trace = os.environ.get('API_TRACE', False)



#--------------------
#- Server Mechanics -
#--------------------

#- load application code before the worker processes are forked. -
preload_app = os.environ.get('API_PRELOAD_APP', c.preload_app)

#- disables the use of sendfile() -
sendfile = os.environ.get('API_SENDFILE', c.sendfile)

#- chdir to specified directory before apps loading. -
chdir = os.environ.get('API_CHDIR', c.chdir)

#- daemonize the gunicorn process. -
daemon = os.environ.get('API_DAEMON', c.daemon)

#- set environment variable (key=value). -
raw_env = os.environ.get('API_RAW_ENV', c.raw_env)

#- filename to use for the pid file -
pidfile = os.environ.get('API_PIDFILE', c.pidfile)

#- directory to use for the worker heartbeat temporary file -
worker_tmp_dir = os.environ.get('API_WORKER_TMP_DIR', c.worker_tmp_dir)

#- switch worker processes to run as this user -
user = os.environ.get('API_USER', c.user)

#- switch worker process to run as this group -
group = os.environ.get('API_GROUP', c.group)

#- bit mask for the file mode on files written by gunicorn -
umask = os.environ.get('API_UMASK', c.umask)

#- directory to store temporary request data as they are read -
tmp_upload_dir = os.environ.get('API_TMP_UPLOAD_DIR', c.tmp_upload_dir)

#- dictionary containing headers and values that the front-end proxy uses to indicate https requests -
secure_scheme_headers = os.environ.get('API_SECURE_SCHEME_HEADERS', c.secure_scheme_headers)

#-----------
#- Logging -
#-----------

#- access log file to write to -
accesslog = os.environ.get('API_ACCESSLOG', c.accesslog)

#- access log format -
access_log_format = os.environ.get('API_ACCESS_LOG_FORMAT', c.access_log_format)

#- granularity of error log outputs.  debug info warning error critical -
loglevel = os.environ.get('API_LOGLEVEL', c.loglevel)

#- redirect stdout/stderr to error log -
capture_output = os.environ.get('API_CAPTURE_OUTPUT', c.capture_output )

#- logger you want to use to log events in gunicorn -
logger_class = os.environ.get('API_LOGGER_CLASS', c.logger_class)

#- log config file to use. gunicorn uses the standard python logging module’s configuration file format -
logconfig = os.environ.get('API_LOGCONFIG', c.logconfig)

#- address to send syslog messages -
syslog_addr = os.environ.get('API_SYSLOG_ADDR', c.syslog_addr)

#- send gunicorn logs to syslog -
syslog = os.environ.get('API_SYSLOG', c.syslog)

#- makes gunicorn use the parameter as program-name in the syslog entries -
syslog_prefix = os.environ.get('API_SYSLOG_PREFIX', c.syslog_prefix)

#- syslog facility name -
syslog_facility = os.environ.get('API_SYSLOG_FACILITY', c.syslog_facility)

#- enable inheritance for stdio file descriptors in daemon mode -
enable_stdio_inheritance = os.environ.get('API_ENABLE_STDIO_INHERITANCE', c.enable_stdio_inheritance)

#- host:port of the statsd server to log to -
statsd_host = os.environ.get('API_STATSD_HOST', c.statsd_host)

#- prefix to use when emitting statsd metrics (a trailing . is added, if not provided) -
statsd_prefix = os.environ.get('API_STATSD_PREFIX', c.statsd_prefix)

#- a base to use with setproctitle for process naming -
proc_name = os.environ.get('API_PROC_NAME', c.proc_name)

#- internal setting that is adjusted for each type of application -
default_proc_name = os.environ.get('API_DEFAULT_PROC_NAME', c.default_proc_name)
