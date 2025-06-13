from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sociedades.views import SociedadeViewSet, MembroViewSet

router = DefaultRouter()
router.register(r'sociedades', SociedadeViewSet)
router.register(r'membros', MembroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),# Rotas da API
]
