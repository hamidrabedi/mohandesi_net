import multiprocessing

bind = "0.0.0.0:32226"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
worker_connection = 1000
timeout = 100

preload_app = False
daemon = False

# user = 'django'
# group = 'django'

# ssl
# keyfile=
# certfile=
# ssl_version=

# log
accesslog = '-'
# log_level = 'info'
# access_log_format =
errorlog = '-'

# debug
reload = False
reload_engine = 'auto'
# reload_extra_file = []