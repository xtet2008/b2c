# -*- coding: utf8 -*-

import datetime
# import redis

# constants
DEBUG = False
TESTING = False
TIMEZONE = 'Asia/Shanghai'
# HOST = 'www.1tai.com'

# database
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database'
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_MAX_OVERFLOW = 150
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session
# SECRET_KEY = 'y$*=-4xj(j@d^v=bpq##l8i&!&u&k(^b)j1=uvf$buic(-2=_2))'
# SESSION_TYPE = 'redis'
# SESSION_REDIS = redis.Redis(host='cache1')
# SESSION_COOKIE_NAME = 'session'
# PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=60)


# cache
# CACHE_HOST = 'cache1'
# CACHE_PORT = 6379
# CACHE_PASSWORD = "123456"
# CACHE_DB = 0
# CACHE_PREFIX = 'to_cache:'

# nosql
# NOSQL_HOST = 'nosql1'
# NOSQL_PORT = 6379
# NOSQL_DB = 0
# NOSQL_PREFIX = 'to_nosql:'


# MANAGER_COMMANDS = (
#     'b2c.commands.common',
#     'b2c.commands.es_sync',
#     'b2c.commands.hot_search_statistic'
# )


# INTRA_TOKEN_REQUIRED = True
# INTRA_TOKEN_MAP = {
#     # (token, third project name)
#     'default': 'all',
# }


# babel
# BABEL_DEFAULT_TIMEZONE = TIMEZONE
# BABEL_DEFAULT_LOCALE = 'en'
# BABEL_TRANSLATION_DIRECTORIES = '../configs/current/translations'


# qiniu
# QINIU_ACCESS_KEY = 'RqRHNMDNh4EklCQwTqUDWJrTnLPnHidoRBGjTFH0'
# QINIU_SECRET_KEY = 'xZ104y1OTOgmcBOppRtwabiY32xeuNkLC5HOJrUf'
# QINIU_BUCKET = 'theone-smartpiano4'
# QINIU_BASIC_URL = ''
# QINIU_CUSTOM_URLS = ['oc3cteha2.bkt.clouddn.com', ]


# ldap
# LDAP_HOST = ''
# LDAP_USERNAME = ''
# LDAP_PASSWORD = ''
# LDAP_BASE_DN = 'dc=xiaoyezi,dc=com'
# LDAP_USER_OBJECT_FILTER = '(&(objectclass=person)(uid=%s))'
# LDAP_GROUP_OBJECT_FILTER = '(&(objectclass=posixGroup)(cn=%s))'
# LDAP_USE_CACHE = True
# LDAP_CACHE_REDIS = redis.Redis('cache1')
# LDAP_CACHE_TIMEOUT = 60 * 30
# LDAP_CACHE_PREFIX = 'ldap:'
# LDAP_GROUPS = ['piano', 'piano_admin']
# LDAP_AUTH_REQUIRE_GROUP = ['piano']


# sms token
# SMS_TOKEN_SECRET = 'smartpiano4'

# api token
# API_TOKEN_EXPIRED = 2592000  # 30d

# carina

# CARINA_API = 'http://x:5200'
# CARINA_INTRA_TOKEN = 'SmartPiano4'

# 3.x smartpiano API
# SMART_PIANO_V3_API = 'http://smart-v3-api-dev.1tai.com'

# 3.x forget password url
# FROGET_PASSWOD_V3_API = 'https://auth-dev.1tai.com'

# ip source config
# REMOTE_IP_ADDRESS = None

# header
# API_HEADER_REQUIRED = False

# log
LOG_PATH = '/tmp'
LOG_DEFAULT_NAME = 'smartpiano4'

# sentry
# SENTRY_DSN = None

# TEMP PATH
TEMP_PATH = '/tmp'

# SF2_PATH = '/Users/gefengming/PycharmProjects/arachno_modified.sf2'

# Apple Review
# REVIEW_MOBILE = '18888888888'
# REVIEW_CODE = '0000'

# elasticsearch
# ELASTIC_SEARCH_URL = 'http://127.0.0.1:5600'
# ES_INDEX = 'smartpiano4-dev'

# 网友自制曲谱七牛BASE_URL
# PRIVATE_SCORE_QINIU_BASE_URL = 'http://oc3cteha2.bkt.clouddn.com'


# 统计点击量时间间隔
# STATISTICS_INTERVAL = ('*', '*/2')
