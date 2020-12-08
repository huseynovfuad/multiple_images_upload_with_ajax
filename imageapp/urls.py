from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('preloader/',views.preloader,name='preloader'),
]