from django.urls import path
from . import views

app_name = "firehome"

urlpatterns = [
    path('', views.home),
    path('create', views.flame_create, name="create"),
    path('<slug:post>', views.flame_detail, name='detail')
]