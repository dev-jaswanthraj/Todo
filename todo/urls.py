from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('push', views.push, name = "push"),
    path('delete/<int:id>', views.delete , name = "delete")
]