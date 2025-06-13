from django.urls import path

from .views import get_product

app_name = "products"

urlpatterns = [
    path("product/<int:product_id>/", get_product, name="products"),
]
