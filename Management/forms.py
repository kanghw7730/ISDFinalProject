from django import forms
from .models import work_type_setting

class WorktypeForm(forms.ModelForm):
    class Meta:
        model = work_type_setting
        fields = ['work_type_id', 'work_type_name', 'hourly_payroll']