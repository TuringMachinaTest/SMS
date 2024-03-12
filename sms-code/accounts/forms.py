from django import forms

from .models import Account, AccountUser, City

from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout
from crispy_formset_modal.layout import ModalEditFormsetLayout

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column
from crispy_forms.bootstrap import TabHolder, Tab


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'
        
        
class AccountForm(forms.ModelForm):

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
                       Column("partition_name1"),
                       Column("partition_name2"),
                       Column("partition_name3") ,
                    ),
                    Row(
                       Column("partition_name4"),
                       Column("partition_name5"),
                       Column("partition_name6") ,       
                    ),
                    Row(
                       Column("partition_name7"),
                       Column("partition_name8"),
                       Column("partition_name9") ,                     
                    ),
                    Row(
                       Column("partition_name10"),
                       Column(),
                       Column() ,                       
                    ),
                
                ),
                
                Tab("Users",
                    ModalEditFormsetLayout(
                        "InvoiceItemInline",
                        list_display=["name"],
                    ),

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


        
        
class AccountUserForm(forms.ModelForm):

    class Meta:
        model = AccountUser
        fields = '__all__'
        
    def __init__(self, has_permissions=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            TabHolder(
            Tab('Basic',
                    Row(
                        Column('id', css_class="col-1"),
                        Column('name', css_class="col-12"), ))
            )
        )
            