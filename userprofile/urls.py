from django.urls import path

from . import views

app_name = 'userprofile'
urlpatterns = [
    path('<int:user_id>/edit', views.visible, name='profile_page'),
    path('<int:user_id>/update_info', views.update_info, name='update_info'),
    path('<int:user_id>/', views.visible_user_page, name='user_page'),
]

#  Copyright (c) 2020.  Designed TheFox https://github.com/TheFox267
