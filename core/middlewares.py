from django.http import HttpResponseRedirect

class AuthenticationErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 401:
            return HttpResponseRedirect('https://example.com/no-access/')
        return response