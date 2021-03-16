from re import A
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('login/', views.signin, name = 'login'),
    path('logout/',views.signout, name= 'logout'),
    #path('user/',views.user_page, name = 'user_page'), --> uupdated with customer url
    path('signup/', views.signup, name = 'register'),
    path('orders/',views.orders, name = 'order'),
    re_path('customer/(?P<pk>\d+)$', views.customer, name='customer'),
    path('account_setting/',views.account_setting, name='account_setting'),
    path('product/', views.product, name='product'),
    re_path('create_order/(?P<pk>\d+)$', views.create_order, name='create_order'),
    re_path('update_order/(?P<pk>\d+)$', views.update_order, name='update_order'),
    re_path('delete_order/(?P<pk>\d+)$', views.remove_order, name='delete_order'),
    
]
