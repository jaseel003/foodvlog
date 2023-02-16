from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:p_slug>',views.details,name="details"),
    path('search',views.searching,name='search'),
]