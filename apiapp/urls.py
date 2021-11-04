from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('modelviewset', views.UserModelViewSet)


urlpatterns = [
    path('login/', views.LoginViewSet.as_view()),
    path('', include(router.urls))
]
