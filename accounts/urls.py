from django.urls import path

from accounts import views

urlpatterns = [
    path('account_detail/<int:usrid>/', views.AccountList.as_view()),
    path('account_history/<int:accid>/', views.ShowTransferHistory.as_view()),
    path('transfer/', views.MakeTransfer.as_view()),
]