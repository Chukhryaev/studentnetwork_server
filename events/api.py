from events.facade import Facade


def extend_application(app):
    @app.route('/events')
    def events_handler():
        Facade.get_event(1)
        return 'Get events handler'

    @app.route('/event')
    def event_handler():
        return 'Get event handler'
