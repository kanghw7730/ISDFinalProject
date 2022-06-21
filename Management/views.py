from re import T
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import store_information, work_type_setting,worker_information,payroll_management,Login
from .forms import WorktypeForm

def login(request):
    if request.method == "POST":
        login_id = request.POST['login_id']
        login_pw = request.POST['login_pw']

        user_id = Login.objects.get(pk='team4').login_id
        user_pw = Login.objects.get(pk='team4').login_pw


        if (login_id == user_id) and (login_pw == user_pw):
            request.session['manager'] = user_id
            return redirect('store_information')
        else:
            request.session['manager'] = '0'

            #del request.session['manager']
    return render(request, 'Management/login.html')

def add_type(request):
    form = WorktypeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('store_information')

    return render(request, 'Management/type_form.html', {'form': form})

def update_type(request, work_type_id):
    type = work_type_setting.objects.get(work_type_id=work_type_id)
    form = WorktypeForm(request.POST or None, instance=type)

    if form.is_valid():
        form.save()
        return redirect('store_information')

    return render(request, 'Management/type_form.html', {'form': form, 'type': type})


def delete_type(request, work_type_id):
    type = work_type_setting.objects.get(work_type_id=work_type_id)

    if request.method == 'POST':
        type.delete()
        return redirect('store_information')

    return render(request, 'Management/type_delete_confirm.html', {'type': type})

def index(request,store_id):
	return HttpResponseRedirect(request,'Management/store_information.html',{'store_id' :store_id})

def schedule(request,store_id):
	return render(request,'Management/schedule.html',{'store_id' :store_id})

def store_information(request,store_id):
	return render(request,'Management/store_information.html',{'store_id' :store_id})

def worker_management(request,store_id):
	return render(request,'Management/worker_management.html',{'store_id' :store_id})

def work_record(request,store_id):

    store_work_type = list(work_type_setting.objects.filter(store_id=store_id).values())

    work_info_list = []
    for store in store_work_type:
        worker_info = list(worker_information.objects.filter(worktype_id=store['work_type_id']).values())
        work_info_list.append(worker_info)
    
    for worker_list in work_info_list:    
        for worker in worker_list:
            working_hours = worker['working_hours']
            hour_pay = 0
            for store in store_work_type:
                print('store',store)
                if store['work_type_id'] == worker['worktype_id_id']:
                    hour_pay =store['hourly_payroll']
            worker['total_work_pay']= working_hours*hour_pay
            worker['total_work_hour']=working_hours
            if working_hours >= 60:
                bonus_pay = hour_pay * 7.5 * 4
            else:
                bonus_pay = 0
            worker['bonus_pay']=bonus_pay
            worker['total_pay']=worker['total_work_pay'] + worker['bonus_pay']

        total_sum_sum = 0
        for worker_list in work_info_list:    
            for worker in worker_list:
                total_sum_sum += worker['total_pay']

    return render(request, 'Management/work_record.html', {'worker_list': worker_list,'total_sum_sum':total_sum_sum,'store_id' :store_id})

def payroll_management(request, store_id):
    store_work_type = list(work_type_setting.objects.filter(store_id=store_id).values())

    work_info_list = []
    for store in store_work_type:
        worker_info = list(worker_information.objects.filter(worktype_id=store['work_type_id']).values())
        work_info_list.append(worker_info)
    
    for worker_list in work_info_list:    
        for worker in worker_list:
            working_hours = worker['working_hours']
            hour_pay = 0
            for store in store_work_type:
                if store['work_type_id'] == worker['worktype_id_id']:
                    hour_pay =store['hourly_payroll']
            worker['total_work_pay']= working_hours*hour_pay
            worker['total_work_hour']=working_hours
            if working_hours >= 60:
                bonus_pay = hour_pay * 7.5 * 4
            else:
                bonus_pay = 0
            worker['bonus_pay']=bonus_pay
            worker['total_pay']=worker['total_work_pay'] + worker['bonus_pay']

        total_sum_sum = 0
        for worker_list in work_info_list:    
            for worker in worker_list:
                total_sum_sum += worker['total_pay']

    return render(request, 'Management/payroll_management.html', {'worker_list': worker_list,'total_sum_sum':total_sum_sum,'store_id' :store_id})


#def time_slot(request, storeinformation):
	#return render(request, 'Management/update.html', context)
	




