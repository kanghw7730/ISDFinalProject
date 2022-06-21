from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/', views.login,name='login'),
    path('add/', views.add_type,name='add_type'),
    path('update/<int:work_type_id>', views.update_type,name='update_type'),
    path('delete/<int:work_type_id>', views.delete_type,name='delete_type'),
    path('payroll_management/<int:store_id>', views.payroll_management, name='payroll_management'),
    path('work_record/<int:store_id>', views.work_record, name='work_record'),
    path('schedule/<int:store_id>', views.schedule, name='schedule'),
    path('store_information/<int:store_id>', views.store_information, name='store_information'),
    path('worker_management/<int:store_id>', views.worker_management, name='worker_management')
]