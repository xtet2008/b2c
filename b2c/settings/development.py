# -*- coding: utf8 -*-

from b2c.settings.base import *

ENV = 'development'
# DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://root:abcd1234@xtet.xyz/b2c'


LOG_PATH = 'd:/temp'
LOG_DEFAULT_NAME = 'b2c'

# sentry
# SENTRY_DSN = None

# TEMP PATH
TEMP_PATH = 'd:/temp'