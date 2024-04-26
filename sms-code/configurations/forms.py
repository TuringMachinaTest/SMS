from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column
from extra_views import InlineFormSetFactory
from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout, ModalEditFormsetLayout
from crispy_forms.bootstrap import TabHolder, Tab

from accounts.utils import get_partitions_choices
from configurations.utils import get_action_choices

from .models import AlarmCode, Device, Schedule
from django.utils.translation import gettext as _


class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = '__all__'
        
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()

        if not details:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
            for field in self.fields:
                self.fields[field].disabled = True
                
                
                
class AlarmCodeForm(forms.ModelForm):    
    class Meta:
        model = AlarmCode
        fields = '__all__' 
    
    def __init__(self, details = False, account_id = -1,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            TabHolder(
                Tab('Test 1', 
                    Row(
                        Column("partition"),
                    ),
                    Row(
                        Column("code", css_class="col-4"),
                        Column("description", css_class="col-8")
                    ),
                    Row(
                      Column("decryption_type")  
                    ),
                ),
                Tab('Test 2', ),
            )
        )
        
        self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(account_id))
        
        self.fields['action_101'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_102'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_103'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_104'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_105'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_106'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_107'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_108'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_109'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_110'] = forms.ChoiceField(choices=get_action_choices(account_id))

        self.fields['action_201'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_202'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_203'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_204'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_205'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_206'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_207'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_208'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_209'] = forms.ChoiceField(choices=get_action_choices(account_id))
        self.fields['action_210'] = forms.ChoiceField(choices=get_action_choices(account_id))


        # Disable submit button for non-admin users
        if not details:
            for field in self.fields:
                self.fields[field].disabled = True             


class AlarmCodeInlineFormSet(InlineFormSetFactory):
   
    model = AlarmCode
    form_class = AlarmCodeForm
    factory_kwargs = {"extra": 0}
    
    def get_formset_kwargs(self):
        kwargs = super(AlarmCodeInlineFormSet, self).get_formset_kwargs()

        #self.formset_kwargs = { 'form_kwargs' : { 'account_id' : kwargs['instance'].id}}
        # Add any additional parameters you want to pass to the form
        #print(kwargs)
        
        kwargs['form_kwargs'] = {}
        if kwargs['instance']:
            kwargs['form_kwargs']['account_id'] = kwargs['instance'].id 
        kwargs['form_kwargs']['details'] = True
                
        return kwargs
    
    
class ScheduleForm(forms.ModelForm):

    opening_saturday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Opening"))
    closing_saturday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Closing"))

    opening_sunday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Opening"))
    closing_sunday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Closing"))

    opening_monday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Opening"))
    closing_monday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Closing"))

    opening_tuesday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Opening"))
    closing_tuesday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Closing"))

    opening_wednesday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Opening"))
    closing_wednesday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Closing"))

    opening_thursday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Opening"))
    closing_thursday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Closing"))

    opening_friday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Opening"))
    closing_friday = forms.DateField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), required=False, label=_("Closing"))
    
    class Meta:
        model = Schedule
        fields = '__all__'
        
    def __init__(self, details = False, account_id=-1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column("partition", css_class="col-4"),
            ),
            Row(
                Column("is_open_saturday", css_class="col-2"),
                Column("opening_saturday", css_class="col-3"),
                Column("delay_opning_saturday", css_class="col-2"),
                Column("closing_saturday", css_class="col-3"),
                Column("delay_closing_saturday", css_class="col-2"),
            ),
            Row(
                Column("is_open_sunday", css_class="col-2"),
                Column("opening_sunday", css_class="col-3"),
                Column("delay_opning_sunday", css_class="col-2"),
                Column("closing_sunday", css_class="col-3"),
                Column("delay_closing_sunday", css_class="col-2"),
            ),
            Row(
                Column("is_open_monday", css_class="col-2"),
                Column("opening_monday", css_class="col-3"),
                Column("delay_opning_monday", css_class="col-2"),
                Column("closing_monday", css_class="col-3"),
                Column("delay_closing_monday", css_class="col-2"),
            ),
            Row(
                Column("is_open_tuesday", css_class="col-2"),
                Column("opening_tuesday", css_class="col-3"),
                Column("delay_opning_tuesday", css_class="col-2"),
                Column("closing_tuesday", css_class="col-3"),
                Column("delay_closing_tuesday", css_class="col-2"),
            ),
            Row(
                Column("is_open_wednesday", css_class="col-2"),
                Column("opening_wednesday", css_class="col-3"),
                Column("delay_opning_wednesday", css_class="col-2"),
                Column("closing_wednesday", css_class="col-3"),
                Column("delay_closing_wednesday", css_class="col-2"),
            ),
            Row(
                Column("is_open_thursday", css_class="col-2"),
                Column("opening_thursday", css_class="col-3"),
                Column("delay_opning_thursday", css_class="col-2"),
                Column("closing_thursday", css_class="col-3"),
                Column("delay_closing_thursday", css_class="col-2"),
            ),
            Row(
                Column("is_open_friday", css_class="col-2"),
                Column("opening_friday", css_class="col-3"),
                Column("delay_opning_friday", css_class="col-2"),
                Column("closing_friday", css_class="col-3"),
                Column("delay_closing_friday", css_class="col-2"),
            ),
        )
        
        self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(account_id))


class ScheduleInlineFormSet(InlineFormSetFactory):
   
    model = Schedule
    form_class = ScheduleForm
    factory_kwargs = {"extra": 0}
    
    def get_formset_kwargs(self):
        kwargs = super(ScheduleInlineFormSet, self).get_formset_kwargs()

        #self.formset_kwargs = { 'form_kwargs' : { 'account_id' : kwargs['instance'].id}}
        # Add any additional parameters you want to pass to the form
        #print(kwargs)
        
        kwargs['form_kwargs'] = {}
        if kwargs['instance']:
            kwargs['form_kwargs']['account_id'] = kwargs['instance'].id 
        kwargs['form_kwargs']['details'] = True
                
        return kwargs
