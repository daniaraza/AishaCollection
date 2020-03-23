from django.urls import path
from . import views
from backend.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib import admin
from .views import emailView
from .views import index
from django.conf.urls import url

urlpatterns = [
    path('', views.aboutus, name='aboutus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login', index),
    path('privacy/', views.privacy, name='privacy'),
    path('information/', views.information, name='information'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('products/ss', views.products_sabyasachi, name='products_sabyasachi'),
    path('products/manish', views.products_manish, name='products_manish'),
    path('products/ritu', views.products_ritu, name='products_ritu'),
    path('products/saree', views.products_saree, name='products_saree'),
    path('products/men', views.products_men, name='products_men'),
    path('products/accessories', views.products_accessories, name='products_accessories'),
    path('products/price', views.products_price, name='products_price'),
    path('products/details/', views.products_details, name='products_details'),
    path('products/showdetails/', views.show_details, name='show_details'),
    # path('index/', views.index, name = 'index'),
    path('allproducts/', views.allproducts, name='allproducts'),
    # path('home/upload/', views.upload, name='upload-bride'),
    path('upload/', views.upload, name='upload-bride'),
    path('allproducts/update/<int:bride_id>', views.update_bride, name = 'update_bride'),
    path('allproducts/delete/<int:bride_id>', views.delete_bride),
    path('allproducts/upload/<int:bride_id>', views.upload),
    path('email/', emailView, name='email'),
    path('stores/', views.stores, name='stores'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('special/', views.special, name='special'),
    # path('products/showdetails/cart/', views.cart_detail, name='cart_detail'),
    # path('cartadd/', views.cart_add, name='cart_add'),
    path('cart/', views.cart, name='cart'),
    # path('remove/(<product_id>/', views.cart_remove, name='cart_remove'),
    ]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)