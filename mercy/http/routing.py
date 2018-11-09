from werkzeug import wrappers

from mercy.http import responses


MERCY_QUOTE = "I'm taking care of you."


class Router(object):
    """ decides which controller to execute for a request """

    def __init__(self, *, environment):
        self.environment = environment

    def __call__(self, request):
        return responses.Response(MERCY_QUOTE)
