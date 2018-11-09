from werkzeug import serving
from werkzeug import wrappers

from mercy import utils
from mercy.http import routing


class Service(object):
    """ A Service is something that listens for and response to requests """

    def __init__(self, router=None):
        if router is None:
            router = routing.Router

        self.router = router

    def create_router(self, environment, *, router=None):
        """ Create a new router for this service to use """

        if router is None:
            router = self.router

        return utils.objects.ensure_instance(router, environment=environment)

    def create_application(self, environment, *, router=None):
        """ Create a new Werkzeug application """
        if router is None:
            router = self.create_router(environment)

        return wrappers.Request.application(router)

    def __call__(self, environment, *args):
        print(environment, *args)
        return self.create_application(environment)

    @classmethod
    def listen(
        self,
        hostname='localhost', port=3030,
        via=serving.run_simple, router=None,
        *args, **kwargs
    ):

        """ Provides a quick method for listening with or without a Service instance.

        This will start a service by calling `via` with your hostname, port,
        and any additional args and kwargs provided via *args and **kwargs.

        """

        service = utils.objects.ensure_instance(self, router=router)
        application = wrappers.Request.application(service)
        return via(hostname, port, application, *args, **kwargs)
