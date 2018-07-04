# -*- coding: utf8 -*-

# from werkzeug.contrib.fixers import ProxyFix
from flask_script import Manager
from b2c import create_app

from flask_migrate import Migrate, MigrateCommand

from b2c.extensions import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
# app will use the actual `REMOTE_ADDR` when running being proxy such as nginx
# app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    # from b2c.commands import install_commands


    # install_commands(manager)
    # manager.add_command('db', MigrateCommand)  # database management, db has already used for lyra.commands.database
    manager.run()