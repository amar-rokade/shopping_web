
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('',views.ProductListView.as_view(),name="home"),
    path('signup/seller/',views.SellerSignUpView.as_view(),name="seller_signup"),
    path('signup/buyer/',views.BuyerSignUpView.as_view(),name="buyer_signup"),
    path('logout/',views.LogOut,name="logout"),
    path('login/',views.LogIn,name="login"),
    path('Seller/item_list',views.SellerView,name="sellerview"),
    path('Buyer/item_list',views.BuyerView,name="buyerview"),
    path('new_item/add/',views.ItemFormView,name="itemform"),
    path('add_to_cart/',views.AddCartView,name="add_to_cart"),
    path('<int:pk>/buy/',views.BuyView,name="buy"),
    path('search/result/',views.SearchResultView,name="search"),
    path('<int:pk>/update/',views.ItemUpdateView.as_view(),name="update"),
    path('<int:pk>/delete/',views.ItemDeleteView.as_view(),name="delete"),
]
