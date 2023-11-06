from django.urls import path

from adminpanel import views

urlpatterns= [
        path('create_employe/',views.CreateEmployee.as_view()),
        path('show_employess/',views.ShowEmployess.as_view()),
        path('show_employess/<int:pk>/',views.ShowEmployByID.as_view()),
        path('activate_user/<int:usrid>/',views.ActivateUser.as_view()),
    ]