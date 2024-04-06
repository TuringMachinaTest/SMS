from django import forms
from extra_views import InlineFormSetFactory

from accounts.utils import get_partitions_choices

from .models import DecryptedEvent, RawEvent

from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout
from crispy_formset_modal.layout import ModalEditFormsetLayout

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column
from crispy_forms.bootstrap import TabHolder, Tab

from django_select2 import forms as s2forms

from phonenumber_field import formfields, widgets

class DecryptedEventForm(forms.ModelForm):

    class Meta:
        model = DecryptedEvent
        fields = '__all__'
        
    def __init__(self, details=False, account_id = -1,  *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('protocole'),
                Column('receiveer_no'),
                Column('line_no'),  
                Column('partition'),              
            ),
            Row(
                Column('alarm_code', css_class="col-3"),
                Column('status', css_class="col-3"),
                Column('note'),
            )
        )
        
        self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(account_id))

        if not details:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True
               

class RawEventForm(forms.ModelForm):

    class Meta:
        model = RawEvent
        fields = '__all__'
        
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()

        for field in self.fields:
            self.fields[field].disabled = True
               