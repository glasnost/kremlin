The Kremlin Magical Everything System
======================================

The Magical Everything System does Everything.

Features:
---------
* Image Board
* Boredom Inhibitor
* Science Experiment
* Operating System Overview
* Arguably alive

.. danger:: May contain traces of Knifacode(tm)


Requirements:
-------------

These are the requirements for running the application. Unless you are
sitting there reading this from a tagged release archive, it probably will 
not be entirely accurate.


* Python 2.7
* virtualenv_ is strongly recommended
* For production deployment, a decent web server supporting WSGI


         -- or--

* gunicorn_ behind something like nginx_.

Python Modules:
~~~~~~~~~~~~~~~

* Flask_ - Amazing Python Microframework Extraordinaire
* Jinja2_ - Templating Engine
* Pillow_ (recommended) _or_ PIL_ - Image manipulation library
* SQLAlchemy_ - Declarative ORM
* WTForms_ - Web form helper/library

Flask Modules:
~~~~~~~~~~~~~~~

.. note:: Being a microframework, it doesn't do much.

* Flask-SQLAlchemy
* Flask-Uploads
* Flask-WTF


Very Hastily Written™ Hacker's Guide to Poking at the Source
-------------------------------------------------------------

1. ``$ mkdir ~/.python-envs/``
2. ``$ virtualenv --distribute --no-site-packages ~/.python-envs/kremlin``
3. ``$ source ~/.python-envs/kremlin/bin/activate``
4. ``(kremlin)$ pip install -r requirements.txt``
5. ``(kremlin)$ git clone https://github.com/glasnost/kremlin.git kremlin``
6. ``(kremlin)$ cd kremlin``
7. ``(kremlin)$ cp kremlin-example.cfg kremlin.cfg && vim kremlin.cfg``
8. ``(kremlin)$ KREMLIN_CONFIGURATION=$(pwd)/kremlin.cfg python runserver.py``

.. Mac OS X:: you will need additional dependencies before Pillow builds
   correctly.

Run this before you run ``pip install`` above:

``brew install libjpeg``

You will of course need Brew_ installed.

.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _gunicorn: http://gunicorn.org/
.. _nginx: http://nginx.org/

.. _Flask: http://flask.pocoo.org/
.. _Jinja2: http://jinja.pocoo.org/docs/
.. _Pillow: http://pypi.python.org/pypi/Pillow
.. _SQlAlchemy: http://www.sqlalchemy.org/
.. _WTForms: http://wtforms.simplecodes.com/docs/dev/

.. _Flask-SQlAlchemy: http://packages.python.org/Flask-SQLAlchemy/
.. _Flask-Uploads: http://packages.python.org/Flask-Uploads/
.. _Flask-WTF: http://packages.python.org/Flask-WTF/

.. _Brew: http://brew.sh

