
from django.urls import  path
from products import views


urlpatterns = [
    path('hello/',views.hello),
    path('allproducts/',views.getproducts),
    path('products/<int:product_id>/', views.get_product_by_id),
    path('product/', views.save_product, name='save_product'),

]
