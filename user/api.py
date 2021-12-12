def extend_application(app):
    @app.route('/my')
    def my_handler():
        return 'Hey! It is you!'
