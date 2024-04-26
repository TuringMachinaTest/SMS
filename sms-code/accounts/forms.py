from .utils import get_partitions_choices
from django import forms
from extra_views import InlineFormSetFactory

from .models import Account, AccountNote, AccountUser, City, Group, InstallationCompany, Zone

from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout, ModalEditFormsetLayout

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column
from crispy_forms.bootstrap import TabHolder, Tab

from django_select2 import forms as s2forms

from phonenumber_field import formfields, widgets
from django.utils.translation import gettext as _


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'
        
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()

        if not details:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()

        if not details:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True             

                
class InstallationCompanyForm(forms.ModelForm):

    class Meta:
        model = InstallationCompany
        fields = '__all__'
    
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()

        if not details:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True
              
                
class AccountForm(forms.ModelForm):

    installation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    installation_company_phone_number1 = formfields.PhoneNumberField(region="SY", max_length=20, required=False, widget=widgets.TextInput(attrs={'readonly': 'True'}))
    installation_company_phone_number2 = formfields.PhoneNumberField(region="SY", max_length=20, required=False, widget=widgets.TextInput(attrs={'readonly': 'True'}))
    
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, widget=s2forms.ModelSelect2Widget(
        search_fields = [
            "name__icontains",
        ],
    ))
    
    installation_company = forms.ModelChoiceField(queryset=InstallationCompany.objects.all(), required=False, widget=s2forms.ModelSelect2Widget(
        search_fields = [
            "name__icontains",
        ],
    ))
    
    copy_alarm_codes_from = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=Account,
            search_fields=['id__icontains', 'name__icontains'],
        )
    )
    
    class Meta:
        model = Account
        fields = '__all__'
        
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Basic'),
                    Row(
                        Column('id', css_class="col-1"),
                        Column('name', css_class="col-3"), 
                        Column('city'),
                        Column('zip_code'), 
                    ),
                    Row(
                        Column('email'),
                        Column('address_line1', css_class="col-8"),
                    ),
                    Row(
                        Column('phone_number1'),
                        Column('address_line2', css_class="col-8"), 
                        
                    ),
                    Row(
                        Column('whatsapp_number'),
                        Column('address_line3', css_class="col-8"),
                    ),
                    
                    Row(
                        Column('phone_number2'),
                        Column(css_class="col-8"),
                    ),
                    
                ),
                Tab(_('Misc'),
                    Row(
                        Column('security_number'),
                        Column('memo', css_class="col-8")
                    ),
                    Row(
                        Column('police_number1'),   
                        Column('fire_dept_number1'), 
                        Column('emergency_number1'), 
                    ),
                    Row(
                        Column('police_number2'), 
                        Column('fire_dept_number2'),
                        Column('emergency_number2'), 
                    ),
                    Row(
                        Column('police_number3'),
                        Column('fire_dept_number3'), 
                        Column('emergency_number3'), 
                    )
                ),
                Tab(_('Partitions'),
                    Row(
                       Column("partition_name0"),
                       Column("partition_name1"),
                       Column("partition_name2"),
                       Column("partition_name3") ,
                    ),
                    Row(
                       Column("partition_name4"),
                       Column("partition_name5"),
                       Column("partition_name6") , 
                       Column("partition_name7"),
      
                    ),
                    Row(
                       Column("partition_name8"),
                       Column("partition_name9") , 
                       Column("partition_name10"),
                       Column(),                    
                    ),
                    Row(
                   
                    ),
                
                ),
                                
                Tab(_("Alarm Codes"),
                    ModalEditFormsetLayout(
                        "AlarmCodeInlineFormSet",
                        list_display=["code", "description" ],
                    ),
                ),
                Tab(_("Copy Alarm Codes"),
                    Row(
                        Column("copy_alarm_codes"),
                        Column("copy_alarm_codes_from"),
                    ),
                ),
                
                Tab(_("Schedules"),
                    ModalEditFormsetLayout(
                        "ScheduleInlineFormSet",
                        list_display=["partition", "is_open_saturday", "is_open_sunday", "is_open_monday", "is_open_tuesday", "is_open_wednesday", "is_open_thursday", "is_open_friday"],
                    ),
                ),
                                
                Tab(_("Zones"),
                    ModalEditFormsetLayout(
                        "ZoneInlineFormSet",
                        list_display=["partition", "name", "code", ],
                    ),

                ),
                
                Tab(_("Users"),
                    ModalEditFormsetLayout(
                        "AccountUserInlineFormSet",
                        list_display=["name", "title", "partition", "phone_number1", "phone_number2", "phone_number3"],
                    ),

                ),
                
                Tab(_("Installation"),
                    Row(
                       Column("installation_company"),
                       Column("installation_date"),                  
                    ),
                    Row(
                        Column("installation_company_phone_number1"), 
                        Column("receiver_phone_number"),    
                    ),
                    Row(
                        Column("installation_company_phone_number2"), 
                        Column("transmitter_phone_number"),    
                    ),
                    Row(
                       Column("installation_note"), 
                    )
                ),
                Tab(_("Groups"),
                    Row(
                        Column("groups")
                    ),
                ),
                
                Tab(_("Notes"),
                    ModalEditFormsetLayout(
                        "AccountNoteInlineFormSet",
                        list_display=["note", "timer"],
                    ),
                ),
                
                Tab(_("Service Orders"),
                    ModalEditFormsetLayout(
                        "ServiceOrderInlineFormSet",
                        list_display=["summary", "status"],
                    ),
                ),
            ),
        )
        
        # Disable submit button for non-admin users
        if not details:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True
                
            # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary', disabled=True))
            
        instance = kwargs.pop('instance', None)
        
        if instance:
            if instance.installation_company:
                self.fields["installation_company_phone_number1"].initial = instance.installation_company.phone_number1
                self.fields["installation_company_phone_number2"].initial = instance.installation_company.phone_number2



class DatePicker(forms.widgets.DateInput):
    input_type = 'date'
    
    
class TimePicker(forms.widgets.TimeInput):
    input_type = 'time'
        
        
class AccountUserForm(forms.ModelForm):
    
    holiday_begins = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    holiday_ends = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    
    class Meta:
        model = AccountUser
        fields = '__all__'
        
    def __init__(self, details = False, account_id = -1,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            TabHolder(
                Tab(_("Information"),
                    Row(
                        Column('partition',),
                    ),
                    Row(
                        Column('code', css_class="col-4"),
                        Column('name', css_class="col-8"),
                    ),
                    Row(
                        Column('in_out_codes'),
                        Column('password'), 
                    ),
                    Row(
                        Column('phone_number1'),
                        Column('title'), 
                    ),
                    Row(
                        Column('phone_number2', css_class="col-6"),
                    ),
                    Row(
                        Column('phone_number3', css_class="col-6"),
                    ),
                ),
                Tab(_("Control"),
                    Row(
                        Column('holiday_begins'),
                        Column('holiday_ends'),
                    ),            
                    Row(
                        Column('keypad_code'),
                        Column('hot_user'),
                    ),
                    Row(
                        Column('authorized_days_sun'),
                        Column('authorized_days_thu'),
                    ),
                    Row(
                        Column('authorized_days_mon'),
                        Column('authorized_days_fri'),
                    ),
                   Row(
                        Column('authorized_days_tue'),
                        Column('authorized_days_sat'),
                    ),
                    Row(
                        Column('authorized_days_wed', css_class="col-6"),
                    ),
                ),
            ),
        )
        
        self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(account_id))
        
        # Disable submit button for non-admin users
        if not details:
            for field in self.fields:
                self.fields[field].disabled = True             
    
class AccountUserInlineFormSet(InlineFormSetFactory):
   
    model = AccountUser
    form_class = AccountUserForm
    factory_kwargs = {"extra": 0}
    
    def get_formset_kwargs(self):
        kwargs = super(AccountUserInlineFormSet, self).get_formset_kwargs()

        #self.formset_kwargs = { 'form_kwargs' : { 'account_id' : kwargs['instance'].id}}
        # Add any additional parameters you want to pass to the form
        #print(kwargs)
        
        kwargs['form_kwargs'] = {}
        if kwargs['instance']:
            kwargs['form_kwargs']['account_id'] = kwargs['instance'].id 
        kwargs['form_kwargs']['details'] = True
                
        return kwargs
    

class ZoneForm(forms.ModelForm):    
    class Meta:
        model = Zone
        fields = '__all__' 
    
    def __init__(self, details = False, account_id = -1,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column("partition")
            ),
            Row(
                Column("code", css_class="col-4"),
                Column("name", css_class="col-8"),
            )
        )
        
        self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(account_id))
        
        # Disable submit button for non-admin users
        if not details:
            for field in self.fields:
                self.fields[field].disabled = True             


class ZoneInlineFormSet(InlineFormSetFactory):
   
    model = Zone
    form_class = ZoneForm
    factory_kwargs = {"extra": 0}
    
    def get_formset_kwargs(self):
        kwargs = super(ZoneInlineFormSet, self).get_formset_kwargs()

        #self.formset_kwargs = { 'form_kwargs' : { 'account_id' : kwargs['instance'].id}}
        # Add any additional parameters you want to pass to the form
        #print(kwargs)
        
        kwargs['form_kwargs'] = {}
        if kwargs['instance']:
            kwargs['form_kwargs']['account_id'] = kwargs['instance'].id 
        kwargs['form_kwargs']['details'] = True
                
        return kwargs
    
    
class AccountNoteForm(forms.ModelForm):    
    class Meta:
        model = AccountNote
        fields = '__all__' 
    
    def __init__(self, details = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column("note")
            ),
            Row(
                Column("timer", css_class="col-2"),
                Column("timer_interval_minutes", css_class="col-5"),
                Column("timer_interval_hours", css_class="col-5"),
            )
        )
                
        # Disable submit button for non-admin users
        if not details:
            for field in self.fields:
                self.fields[field].disabled = True             


class AccountNoteInlineFormSet(InlineFormSetFactory):
   
    model = AccountNote
    form_class = AccountNoteForm
    factory_kwargs = {"extra": 0}
    
    def get_formset_kwargs(self):
        kwargs = super(AccountNoteInlineFormSet, self).get_formset_kwargs()

        #self.formset_kwargs = { 'form_kwargs' : { 'account_id' : kwargs['instance'].id}}
        # Add any additional parameters you want to pass to the form
        #print(kwargs)
        
        kwargs['form_kwargs'] = {}
        kwargs['form_kwargs']['details'] = True
                
        return kwargs