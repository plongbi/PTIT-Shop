from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginPage, name="login"),      
    path('home/', views.home, name="home"),        
    path('register/', views.register, name="register"),
    path('search/', views.search, name="search"),
    path('category/', views.category, name="category"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('introduce/', views.introduce, name="introduce"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),
    path('update_item/', views.updateItem, name="update_item"),
]
