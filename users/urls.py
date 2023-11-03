from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.UserList.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('user_detail/<int:id>/', views.UserDetail.as_view()),
]