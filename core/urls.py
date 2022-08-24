from django.urls import path, include

# Rest Framework
from rest_framework import routers

# Views
from . import views

router = routers.DefaultRouter()

router.register('reserve', views.UserRoomReserveViewSet, 'reserve')
router.register('room',    views.RoomViewSet,            'room')

app_name = 'core_api'
urlpatterns = [
    path('', include(router.urls)),
]