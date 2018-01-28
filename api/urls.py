from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('bookviewset', views.BookViewSet)
urlpatterns = [
    path('', include(router.urls))
]