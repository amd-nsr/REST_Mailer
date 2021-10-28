from django.contrib.auth import login
from api.models import Subscriber
from django.urls import path
from .views import SubscriberViewSet, login
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)
urlpatterns = [
    path('login/', login),
    path('jwt-auth/',obtain_jwt_token),
]
urlpatterns += router.urls
