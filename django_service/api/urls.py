from django.urls import include, path

urlpatterns = [
    path("", include("products.urls", namespace="products")),
]
