from django.contrib import admin
from .models import store_information, work_type_setting,worker_information,payroll_management,Login

admin.site.register(store_information)
admin.site.register(work_type_setting)
admin.site.register(worker_information)
admin.site.register(payroll_management)
admin.site.register(Login)

# Register your models here.
