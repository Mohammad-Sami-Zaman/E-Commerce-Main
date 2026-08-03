

from django.urls import path
from productmanager.views import *
urlpatterns = [
    path('', login_page, name = 'login'),
    path('signup/', signup, name = 'signup'),
    path('logout_page/', logout_page, name = 'logout_page'),
    path('home/', profile, name = 'home'),



    path('product_catagory/', product_catagory, name = 'product_catagory'),
    path('catagory_add/', catagory_add, name = 'catagory_add'),
    path('catagory_edit/<str:c_id>/', catagory_edit, name = 'catagory_edit'),
    path('catagory_delete/<str:c_id>/', catagory_delete, name = 'catagory_delete'),


    path('product_list/', product_list, name = 'product_list'),
    path('product_add/', product_add, name = 'product_add'),
    path('product_delete/<str:p_id>/', product_delete, name = 'product_delete'),
    path('product_edit/<str:p_id>/', product_edit, name = 'product_edit'),
    path('product_buy/<str:p_id>/', product_buy, name = 'product_buy'),


    path('order_list/', order_list, name = 'order_list'),
    path('customer_list/', customer_list, name = 'customer_list'),
    path('seller_list/', seller_list, name = 'seller_list'),

    path('seller_product_list/', seller_product_list, name = 'seller_product_list'),
    


]
