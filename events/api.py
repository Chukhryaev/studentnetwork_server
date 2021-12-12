def extend_application(app):
    @app.route('/events')
    def events_handler():
        return 'Get events handler'

    @app.route('/event')
    def event_handler():
        return 'Get event handler'
