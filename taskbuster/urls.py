from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from .views import home, home_files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('<filename>(robots.txt)|(humans.txt)', home_files, name='home-files'),
]

urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('admin/', admin.site.urls),
)