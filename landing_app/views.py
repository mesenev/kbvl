from django.http import HttpRequest
from django.template.response import SimpleTemplateResponse


def landing(request: HttpRequest):
    return SimpleTemplateResponse(template='index.html')
