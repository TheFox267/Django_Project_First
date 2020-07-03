from django.urls import path

from . import views

app_name = 'auth'
urlpatterns = [
    path('registration/', views.index, name='reg'),
    path('registration/create_user',views.create_user,name='create_user')
]

#  Copyright (c) 2020.  Designed TheFox https://github.com/TheFox267
