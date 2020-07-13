from django.urls import path,include
from . import views

app_name="accounts"
urlpatterns = [
    path('',views.home,name="home"),
    path('products',views.products,name="products"),
    path('customer/<str:pk>',views.customer,name="customer"),
    path('Add/Order/<str:pk>',views.CreateOrder.as_view(),name="add_order"),
    path('Update/Order/<str:pk>',views.UpdateOrder.as_view(),name="update_order"),
    path('Delete/Order/<str:pk>',views.DeleteOrder.as_view(),name="delete_order"),
]