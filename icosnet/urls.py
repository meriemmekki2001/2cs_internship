from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("icosnet/", include("core.urls")),
    path("admin/", admin.site.urls),
]
