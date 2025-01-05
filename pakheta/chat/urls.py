from django.urls import path
from . import views

urlpatterns = [
    path("birdchat/", views.bird_chatter, name="chat_about_birds"),
]