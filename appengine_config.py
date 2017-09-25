"""
`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.
"""

"""`appengine_config` gets loaded when starting a new application instance."""

from google.appengine.ext import vendor

vendor.add('lib')

