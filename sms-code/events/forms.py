from django import forms
from extra_views import InlineFormSetFactory

from accounts.models import Account
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
from django.utils.translation import gettext as _


class DecryptedEventForm(forms.ModelForm):

    account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=Account,
            search_fields=['id__icontains', 'name__icontains'],
        )
    )
        
    class Meta:
        model = DecryptedEvent
        fields = '__all__'
        
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Event'),
                    Row(
                        Column('account'),
                    ),
                    Row(
                        Column('protocole'),
                        Column('receiveer_no'),
                        Column('line_no'),  
                        Column('partition'),              
                    ),
                    Row(
                        Column('alarm_code', css_class="col-3"),
                        Column(
                            Row(
                                Column('status', css_class="col-12")
                            ),
                            Row(
                                Column('timer'),
                                Column('timer_interval_minnutes'),
                                Column('timer_interval_hours'),
                            ),
                        css_class="col-3"),
                        Column('note'),
                    ),
                ),
                Tab(_('Account Note'),

                    Row(
                        Column('account_note_timer', css_class="col-1"),
                        Column('note_timer_interval_minnutes', css_class="col-1"),
                        Column('note_timer_interval_hours', css_class="col-1"),
                        Column('account_note'),
                    ),
                ),
            )
        )
        
        if 'account' in self.data:
            self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(self.data['account']))
        else:
            self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(-1))

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
               