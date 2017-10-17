from django.conf.urls import url
from landing_app.views import landing
from django.http import HttpResponse

urlpatterns = [
    url(r'^robots.txt$', lambda x: HttpResponse("User-Agent: *\nAllow: *", content_type="text/plain"), name="robots_file"),
    url(r'', landing),
]
