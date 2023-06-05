
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('alura/', include("alura.urls")),
    path('admin/', admin.site.urls),
]
