import os.path
from flask import Flask, send_from_directory
from src.blueprints import calendar, default, task
import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('config/config.ini')

__NETWORK_PORT = config['APP']['PORT']
__NETWORK_HOST = config['APP']['HOST']
__DEBUG = config['APP']['DEBUG']

app = Flask(__name__)
app.register_blueprint(default.default_bp)
app.register_blueprint(calendar.calendar_bp, url_prefix='/api/v1/calendar/')
app.register_blueprint(task.task_bp, url_prefix='/api/v1/task/')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    print('Flask API running on port {0}!'.format(__NETWORK_PORT))
    app.run(host=__NETWORK_HOST, port=__NETWORK_PORT,
            ssl_context='adhoc', debug=__DEBUG)
