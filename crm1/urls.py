from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('login/', views.signin, name = 'login'),
    path('signup/', views.signup, name = 'register'),
    re_path('customer/(?P<pk>\d+)$', views.customer, name='customer'),
    path('product/', views.product, name='product'),
    re_path('create_order/(?P<pk>\d+)$', views.create_order, name='create_order'),
    re_path('update_order/(?P<pk>\d+)$', views.update_order, name='update_order'),
    re_path('delete_order/(?P<pk>\d+)$', views.remove_order, name='delete_order'),
    
]
