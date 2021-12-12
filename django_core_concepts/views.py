from django.http import HttpResponse, HttpResponseRedirect
import json

def home(request):
    response = HttpResponse()
    response.write("Here's the Home page.")

    return response

def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path")