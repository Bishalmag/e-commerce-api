from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CartItemViewSet, CartViewSet, ProductViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('carts', CartViewSet)
router.register('cart-items', CartItemViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]