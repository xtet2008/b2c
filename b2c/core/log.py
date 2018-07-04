# -*- coding: utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler


__all__ = ['init', 'get_logger']
_manager = None


class CallbackFilter(logging.Filter):

    def __init__(self, callback):
        self.callback = callback

    def filter(self, record):
        return self.callback(record)


class LogManager(object):

    def __init__(self, path, default_name, debug=True):
        self.path = path
        self.default_name = default_name
        self.debug = debug
        self._loggers = {}

    def get_fluentd_logger(self):
        pass

    def get_file_logger(self, tag):

        tag = tag if tag else self.default_name
        if tag in self._loggers:
            return self._loggers[tag]

        logger = logging.getLogger(tag)

        if not self.path:
            return logger

        path = '%s/%s.log' % (self.path, tag)
        handler = TimedRotatingFileHandler(path, when='D')
        handler.addFilter(CallbackFilter(lambda x: self.debug))
        handler.setFormatter(
            logging.Formatter('%(asctime)s|%(name)s| %(message)s')
        )
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        self._loggers[tag] = logger

        return logger

    def get_logger(self, tag=''):
        if tag:
            # TODO return self.get_fluentd_logger(tag)
            return self.get_file_logger(tag)
        return self.get_file_logger(tag)


def init(config):
    global _manager
    _manager = LogManager(
        path=config.get('LOG_PATH'),
        default_name=config.get('LOG_DEFAULT_NAME'),
        debug=True,
    )


def get_logger(tag=None):
    if _manager:
        return _manager.get_logger(tag)
    else:
        logging.warn('Logging is not configured properly')
        return logging


def debug_log(msg, *args):
    get_logger(None).debug(msg, *args)
