from django.urls import path
from . import views
from accounts.views import MakeTransfer
urlpatterns = [
    path('lists/', views.UserList.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('register/', views.RegisterUser.as_view()),
    path('transfer/',MakeTransfer.as_view(),name='transfer'),
    path('user_detail/<int:id>/', views.UserDetail.as_view()),
    path('csrf/', views.CSRFView.as_view())
]