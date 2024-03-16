from flask import Flask
from flask import render_template
import os
from . import db, auth, tasks


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "app.sqlite"),
    )

    if test_config is None:
        # load the instance config
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)

    app.add_url_rule("/", endpoint="index")

    return app
