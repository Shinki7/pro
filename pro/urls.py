from django.contrib import admin
from django.urls import include, path, re_path

from .views import index, sidebar, loginView

urlpatterns = [
    re_path(r'^sidebar/', sidebar, name="sidebar"),
    re_path(r'^dashboard/$', index, name="dashboard"),
    re_path(r'^$', loginView, name="login"),
    path('admin/', admin.site.urls),
]