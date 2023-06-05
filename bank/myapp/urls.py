from django.urls import path
from . import views

urlpatterns = [
    path('/home' , views.home , name="home"),
    path('/transfer' , views.transfer , name="transfer"),
    path("/transacions" , views.transactions , name="transactions"),
    path("thanks" , views.thanks , name="thanks"),
    path('' ,views.index , name="index")
]