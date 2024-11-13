from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path tailwind
    path("__reload__/", include("django_browser_reload.urls")),
    #fin path tailwind
    path('', views.index, name="index"),
    path("recordHours/", include("recordHours.urls")),
    path("requestExpiredRegistration/", include("requestExpiredRegistration.urls")),
    path('projects/', include('projects.urls')),
]
