from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='blog-home'),
    path('rasp', rasp, name='rasp'),
    path('create', create, name='create'),
    path('news', news, name='news'),
    path('<int:pk>/delete', Del.as_view(), name='task-delete'),
    path('<int:pk>/update', Upd.as_view(), name='task-update'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/', product_list, name='product-list'),
]
