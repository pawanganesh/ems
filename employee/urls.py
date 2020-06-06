from django.urls import path
from . import views

urlpatterns = [
       path('add_employee/', views.employee_form, name="employee_insert"),
       path('employee_list/', views.employee_list,name="employee_list"),
       path('<int:id>/', views.employee_form, name="employee_edit"),
       path('delete/<int:id>/', views.employee_delete, name="employee_delete"),
       path('individual/<int:id>/', views.view_employee, name="view_employee")
]