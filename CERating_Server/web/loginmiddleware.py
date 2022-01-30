from django.shortcuts import redirect
from django.urls import reverse
import re


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("hello")
        # One-time configuration and initialization.

    def __call__(self, request):
        path = request.path
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        urllist = ['/login']
        if not re.match(r'^/login',path):
            return redirect(reverse("login"))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response