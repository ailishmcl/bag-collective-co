from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bags/', views.bags_index, name='index'),
    path('bags/<int:bag_id>/', views.bag_detail, name='detail'),
    path('bags/create/', views.BagCreate.as_view(), name='bags_create'),
    path('bags/<int:pk>/update/', views.BagUpdate.as_view(), name='bags_update'),
    path('bags/<int:pk>/delete/', views.BagDelete.as_view(), name='bags_delete'),
    path('bags/<int:bag_id>/add_rentals/', views.add_rentals, name='add_rentals'),
]