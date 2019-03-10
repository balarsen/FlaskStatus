import os
import platform

from flask import Flask
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # a simple page that says hello
    @app.route('/status')
    def status():
        out = {
            'architecture': platform.architecture(),
            'dist': platform.dist(),
            'java_ver': platform.java_ver(),
            'libc_ver': platform.libc_ver(),
            'linux_distribution': platform.linux_distribution(),
            'mac_ver': platform.mac_ver(),
            'machine': platform.machine(),
            'node': platform.node(),
            'processor': platform.processor(),
            'python_branch': platform.python_branch(),
            'python_build': platform.python_build(),
            'python_compiler': platform.python_compiler(),
            'python_implementation': platform.python_implementation(),
            'python_revision': platform.python_revision(),
            'python_version': platform.python_version(),
            'python_version_tuple': platform.python_version_tuple(),
            'release': platform.release(),
            'system': platform.system(),
            'uname': platform.uname(),
            'version': platform.version(),
            'win32_ver': platform.win32_ver(),
            'load_average': os.getloadavg()}

        return render_template('status.html', result=out)

    return app
