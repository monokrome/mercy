from mercy.http import services


def execute():
    """ command-line entry point """

    services.Service().listen(use_reloader=True)
