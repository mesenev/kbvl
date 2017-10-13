from django.conf.urls import url
from django.contrib import admin
from landing_app.views import landing

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', landing)
]
