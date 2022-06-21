from django.db import models

class Login(models.Model):
    login_id=models.CharField(max_length=10, primary_key=True)
    login_pw=models.CharField(max_length=15)

class store_information(models.Model):
    store_id=models.CharField(max_length=200,primary_key=True)
    store_name = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    total_worker_num= models.PositiveIntegerField(default=0)
    total_working_hours=models.PositiveIntegerField(default=0)

class work_type_setting(models.Model):
    work_type_id=models.CharField(max_length=200,primary_key=True)
    store_id=models.ForeignKey(store_information, on_delete=models.CASCADE)
    work_type_name= models.CharField(max_length=200)
    hourly_payroll=models.PositiveIntegerField(default=0)

class base_time_slot(models.Model):
    base_time_slot_id=models.CharField(max_length=200,primary_key=True)
    work_type_id= models.ForeignKey(work_type_setting, on_delete=models.CASCADE)
    day_of_week=models.PositiveIntegerField(default=0)
    time=models.PositiveIntegerField(default=0)
    hourly_payroll=models.PositiveIntegerField(default=0)

class worker_information(models.Model):
    work_status_choices= [('Y','Worker'),
                     ('N','Applicant')
                     ]
    worker_id=models.CharField(max_length=200,primary_key=True)
    worker_name=models.CharField(max_length=200)
    work_type=models.CharField(max_length=200)
    worktype_id=models.ForeignKey(work_type_setting, on_delete=models.CASCADE)
    working_hours=models.PositiveIntegerField(default=0)
    available_hours=models.PositiveIntegerField(default=0)
    work_status=models.CharField(max_length=200,choices=work_status_choices)

class payroll_management(models.Model):
    month_choices = [('1', 'January'),
                     ('2', 'February'),
                     ('3', 'March'),
                     ('4', 'April'),
                     ('5', 'May'),
                     ('6', 'June'),
                     ('7', 'July'),
                     ('8', 'August'),
                     ('9', 'September'),
                     ('10', 'October'),
                     ('11', 'November'),
                     ('12', 'December')]

    payroll_management_id=models.CharField(max_length=200,primary_key=True)
    worker_id=models.ForeignKey(worker_information, on_delete=models.CASCADE)
    year=models.PositiveIntegerField(default=0)
    month=models.PositiveIntegerField(choices=month_choices)
    num_of_week=models.PositiveIntegerField(default=0)
    weekly_working_hours=models.PositiveIntegerField(default=0)
    extra_pay=models.PositiveIntegerField(default=0)
    total_weekly_payroll=models.PositiveIntegerField(default=0)


class time_slot(models.Model):
    locked_choices= [('T','True'),
                     ('F','False'),
                     ]

    time_slot_id=models.CharField(max_length=200,primary_key=True)
    base_time_slot_id=models.ForeignKey(base_time_slot, on_delete=models.CASCADE)
    worker_id=models.ForeignKey(worker_information, on_delete=models.CASCADE)
    date=models.CharField(max_length=200)
    locked=models.CharField(max_length=200,choices=locked_choices)
