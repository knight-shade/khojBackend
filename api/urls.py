from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('book-viewset', views.BookViewSet)
router.register('issue-return-viewset', views.IssueReturnViewSet)
router.register('issue-return-history-viewset', views.IssueReturnHistoryViewSet)
urlpatterns = [
    path('', include(router.urls))
]