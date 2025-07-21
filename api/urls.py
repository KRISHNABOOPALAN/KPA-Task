from django.urls import path
from . import views

urlpatterns = [
    path('api/forms/bogie-checksheet', views.submit_bogie_checksheet),
    path('api/forms/wheel-specifications', views.get_wheel_specs),
]