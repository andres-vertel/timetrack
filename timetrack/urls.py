from django.contrib import admin
from django.urls import path, include
from timetrack import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index")
]
