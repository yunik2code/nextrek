from . import views
from django.urls import path

urlpatterns = [
    path('',views.clz_home,name='home'),
    path('info/', views.clz_info, name='info'),
    path('location/', views.clz_location, name='location'),
    path('plantour/', views.clz_plantour, name='plantour'),

]
