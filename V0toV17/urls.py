from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/entries/', views.entries, name='entries'),
    path('<int:user_id>/results/', views.results, name='results'),
    path('<int:user_id>/detail/', views.detail, name='detail'),
]