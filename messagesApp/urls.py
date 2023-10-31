from django.urls import path

from . import views

urlpatterns = [
    path('message/<int:uid>', views.message_create, name='message'),
    path('', views.message_list_users, name='users_message'),
]