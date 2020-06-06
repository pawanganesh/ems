from django.urls import path
from . import views

urlpatterns = [
    path('add_account/', views.add_account, name="add_account"),
    path('manage_user/', views.user_list, name="manage_user"),
    path('<int:id>/', views.add_account, name="update_account"),
    path('delete/<int:id>/', views.delete_user, name="delete_user"),
    path('login/', views.login_account, name="login_account"),
    path('logout/', views.logout_account, name="logout_account"),
]