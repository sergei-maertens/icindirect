Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess icindirect-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/icindirect/log/apache2/error.log"
        CustomLog "/srv/sites/icindirect/log/apache2/access.log" common

        WSGIProcessGroup icindirect-<target>

        Alias /media "/srv/sites/icindirect/media/"
        Alias /static "/srv/sites/icindirect/static/"

        WSGIScriptAlias / "/srv/sites/icindirect/src/icindirect/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-icindirect-<target>]
    user = <user>
    command = /srv/sites/icindirect/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/icindirect/src/icindirect/wsgi/wsgi_<target>.py
    home = /srv/sites/icindirect/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/icindirect/log/uwsgi_err.log
    stdout_logfile = /srv/sites/icindirect/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_icindirect_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/icindirect/log/nginx-access.log;
      error_log /srv/sites/icindirect/log/nginx-error.log;

      location /500.html {
        root /srv/sites/icindirect/src/icindirect/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/icindirect/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/icindirect/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_icindirect_<target>;
      }
    }
