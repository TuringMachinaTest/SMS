from .utils import get_partitions_choices
from django import forms
from extra_views import InlineFormSetFactory

from .models import Account, AccountUser, City, InstallationCompany

from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout
from crispy_formset_modal.layout import ModalEditFormsetLayout

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column
from crispy_forms.bootstrap import TabHolder, Tab

from django_select2 import forms as s2forms

from phonenumber_field import formfields, widgets

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'
        
    def __init__(self, has_permissions=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()


        if has_permissions:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True
                
                
class InstallationCompanyForm(forms.ModelForm):

    class Meta:
        model = InstallationCompany
        fields = '__all__'
    
    def __init__(self, has_permissions=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()


        if has_permissions:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True
     
              
class AuthorWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]
    theme = 'bootstrap4'
    attrs = {'class': 'custom-select'}
              
                
class AccountForm(forms.ModelForm):

    installation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    installation_company_phone_number1 = formfields.PhoneNumberField(region="SY", max_length=20, required=False, widget=widgets.TextInput(attrs={'readonly': 'True'}))
    installation_company_phone_number2 = formfields.PhoneNumberField(region="SY", max_length=20, required=False, widget=widgets.TextInput(attrs={'readonly': 'True'}))
    
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, widget=AuthorWidget())
    
    class Meta:
        model = Account
        fields = '__all__'
        
    def __init__(self, has_permissions=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab('Basic',
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
                Tab('Misc',
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
                Tab('Partitions',
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
                
                Tab("Users",
                    ModalEditFormsetLayout(
                        "AccountUserInlineFormSet",
                        list_display=["name", "title", "partition", "phone_number1", "phone_number2", "phone_number3"],
                    ),

                ),
                
                Tab("Installation",
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
                )
            ),
        )
        
        # Disable submit button for non-admin users
        if has_permissions:
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
        
    def __init__(self, has_permissions = False, account_id = -1,  *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
                Fieldset("Information",
                    Row(
                        Column('partition', css_class="col-4"),
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
                Fieldset("Control",
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
                )
        )
        
        self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(account_id))
        
        # Disable submit button for non-admin users
        if has_permissions:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:           
            for field in self.fields:
                self.fields[field].disabled = True
                
                
class AccountUserInlineFormSet(InlineFormSetFactory):
    model = AccountUser
    form_class = AccountUserForm
    factory_kwargs = {"extra": 0}
    
    #formset_kwargs = {'form_kwargs': { 'account_id': -1 }}
    
    def get_formset_kwargs(self):
        kwargs = super(AccountUserInlineFormSet, self).get_formset_kwargs()

        #self.formset_kwargs = { 'form_kwargs' : { 'account_id' : kwargs['instance'].id}}
        # Add any additional parameters you want to pass to the form
        #print(kwargs)
        
        kwargs['form_kwargs'] = {}
        if kwargs['instance']:
            kwargs['form_kwargs']['account_id'] = kwargs['instance'].id 
        kwargs['form_kwargs']['has_permissions'] = True
                
        return kwargs