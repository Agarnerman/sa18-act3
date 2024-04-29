
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.index, name='product_index'),
    path('show/<int:product_id>/', views.show_product, name='show'),
    path('home/', views.home, name='home')
]