from rest_framework.routers import DefaultRouter
from .views import CriteriaViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'criteria', CriteriaViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]