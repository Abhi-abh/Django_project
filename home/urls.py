from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='home'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('department/',views.department,name='department'),

]
