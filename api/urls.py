from django.urls import path, include
from blogs import views
from rest_framework import routers

from api import views  # Correctly import views from the api app

urlpatterns = [
    path('blogs/', views.BlogList.as_view()),  # Use BlogList from api.views
    path('comments/', views.CommentList.as_view()),

    path('blogs/<int:pk>/', views.BlogDetail.as_view()),  # Use BlogList from api.views
    path('comments/<int:pk>/', views.CommentDetail.as_view())  # Use BlogList from api.views
]