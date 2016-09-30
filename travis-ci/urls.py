from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^manager/', include('test_app.urls'))
]
