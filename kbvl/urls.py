from django.conf.urls import url
from landing_app.views import landing
from django.http import HttpResponse

ggl = "google-site-verification: google0e9c0b4f13a99fcf.html"

urlpatterns = [
    url(r'^robots.txt$', lambda x: HttpResponse("User-Agent: *\nAllow: *", content_type="text/plain"), name="robots_file"),
    url(r'^google0e9c0b4f13a99fcf.html$', lambda x: HttpResponse(ggl, content_type="text/html; charset=utf-8"), name="google_approve"),
    url(r'', landing),
]
