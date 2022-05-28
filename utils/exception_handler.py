import traceback

from django.http import HttpResponse
from django.conf import settings

from user.models import Exceptions

class ErrorHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if exception:
            Exceptions.objects.create(
                url=request.build_absolute_uri(),
                error=repr(exception),
                traceback=traceback.format_exc()
            )