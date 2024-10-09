from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='Index'),
    path('generator/',views.generator,name='Generate'),
    path('explore/',views.explore,name='Explore'),
    path('about/',views.about,name='About Us'),
    
]
