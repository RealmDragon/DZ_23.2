from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, CategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('contacts/', ContactsView.as_view()),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('category/', CategoryListView.as_view(), name='category_list'),
]
