import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler
import os


class Config:
    SECRET_KEY = os.environ.get('CSRF_KEY') or 'hard to guess string'
    BOOTSTRAP_SERVE_LOCAL = True

    @classmethod
    def init_app(cls, app):
        app.config['CACHE_TYPE'] = 'filesystem'
        app.config['CACHE_DIR'] = '/tmp/demo'


    @classmethod
    def logging_setup(cls, app):
        log_file = os.environ.get('/tmp/demo.log')
        # keep up to 10 files, 5MB each
        handler = RotatingFileHandler(log_file, maxBytes=5000000, backupCount=10)
        handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s\t'
                                       '[in %(filename)s:%(funcName)s():%(lineno)d]'))
        app.logger.addHandler(handler)
        if app.debug:
            app.logger.setLevel(logging.DEBUG)
        else:
            app.logger.setLevel(logging.INFO)


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
