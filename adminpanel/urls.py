from django.urls import path

from adminpanel import views

urlpatterns= [
        path('create_employe/',views.CreateEmployee.as_view()),
        path('show_employess/',views.ShowEmployess.as_view()),
        path('show_employess/<int:pk>/',views.ShowEmployByID.as_view()),
        path('activate_user/<int:usrid>/',views.ActivateUser.as_view()),
        path('delete_employee/<int:usrid>/',views.DeleteEmployee.as_view()),
        path('delete_user/<int:usrid>/',views.DeleteUser.as_view()),
        path('user_count/',views.User_count.as_view()),
        path('employe_count/',views.Employe_count.as_view()),
        path('ticket_count/',views.Ticket_count.as_view()),
        path('ticket_list/',views.Ticket_list.as_view()),
        path('ticket_detail/<int:userid>/',views.User_detail.as_view()),

    ]