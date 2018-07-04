import os
from flask import Flask

from b2c.extensions import db
# from b2c.core import log


DEFAULT_APP_NAME = 'b2c'


def config_from_env():
    config_map = {
        'local': 'b2c.settings.localhost',
        'dev': 'b2c.settings.development',
        'prod': 'lyra.settings.production',
    }

    flask_env = os.environ.get('FLASK_ENV', 'dev')
    return config_map.get(flask_env, config_map['dev'])


def create_app(config=None):
    if not config:
        config = config_from_env()

    app = Flask(DEFAULT_APP_NAME)

    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)

    if False:

        configure_path_converter(app)
        configure_i18n(app)
        configure_logging(app)
        configure_elasticsearch(app)
        configure_context_processors(app)
        configure_task(app)
        configure_mongodb(app)

        CORS(app, resources={r"/smart-piano/admin_api/*": {"origins": "*"}})
        CORS(app, resources={r"/smart-piano/web/*": {"origins": "*"}})

    # log.debug_log(' * Runing in %(ENV)s environment' % app.config)

    # @app.teardown_request
    # def shutdown_session(exception=None):
    #     db.session.remove()

    return app


def configure_app(app, config):
    app.config.from_object(config)


def configure_extensions(app):
    db.app = app
    db.init_app(app)


def configure_blueprints(app):
    from b2c.controllers.admin import a_bp
    from b2c.controllers.business import b_bp
    from b2c.controllers.customer import c_bp

    app.register_blueprint(a_bp, url_prefix='/b2c/a')
    app.register_blueprint(b_bp, url_prefix='/b2c/b')
    app.register_blueprint(c_bp, url_prefix='/b2c/c')