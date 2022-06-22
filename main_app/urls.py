from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bags/', views.bags_index, name='index'),
    path('bags/<int:bag_id>/', views.bag_detail, name='detail'),
]