def extend_application(app):
    @app.route('/my')
    def events_handler():
        return 'Hey! It is you!'
