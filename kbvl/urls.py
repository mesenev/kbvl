from django.conf.urls import url
from django.contrib import admin
from landing_app.views import landing
from django.http import HttpResponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots.txt$', lambda x: HttpResponse("User-Agent: *\nAllow: *", content_type="text/plain"), name="robots_file"),
    url(r'', landing),
]
