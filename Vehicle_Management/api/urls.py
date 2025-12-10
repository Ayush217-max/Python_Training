from django.urls import path
from .views import *

urlpatterns = [
    path('vehicles/', vehicles_management),

]