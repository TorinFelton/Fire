from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),
    path('', views.homepage),
    path('firehome/', include('firehome.urls'))
]

urlpatterns += staticfiles_urlpatterns()