from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from firehome import views as firehome_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),
    path('', firehome_views.home, name="home"),
    path('firehome/', include('firehome.urls'))
]

urlpatterns += staticfiles_urlpatterns()