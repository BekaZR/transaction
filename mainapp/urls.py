from django.urls import path

from rest_framework.routers import DefaultRouter as DR

from mainapp.views import PaymentView, UserView


router = DR()
router.register("user", UserView, basename="user")
router.register("payment", PaymentView, basename="payment")

urlpatterns = []

urlpatterns += router.urls