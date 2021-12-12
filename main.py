from flask import Flask

import events.api as events_api

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Up and running!'


events_api.extend_application(app)
