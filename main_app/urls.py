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
    # renter urls
    path('renters/', views.RenterList.as_view(), name='renters_index'),
    path('renters/<int:pk>/', views.RenterDetail.as_view(), name='renters_detail'),
    path('renters/create/', views.RenterCreate.as_view(), name='renters_create'),
    path('renters/<int:pk>/update/', views.RenterUpdate.as_view(), name='renters_update'),
    path('renters/<int:pk>/delete/', views.RenterDelete.as_view(), name='renters_delete'),
    # associating and un-associating bag and renter
    path('bags/<int:bag_id>/assoc_renter/<int:renter_id>/', views.assoc_renter, name='assoc_renter'),
    path('bags/<int:bag_id>/disassoc_renter/<int:renter_id>/', views.disassoc_renter, name='disassoc_renter'),
]