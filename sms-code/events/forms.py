from django import forms
from extra_views import InlineFormSetFactory

from accounts.models import Account, AccountUser, Zone
from accounts.utils import get_partitions_choices
from configurations.models import AlarmCode

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
        ),
        label=_("Account")
    )

    alarm_code = forms.ModelChoiceField(
        queryset=AlarmCode.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=AlarmCode,
            dependent_fields={'account': 'account', 'partition': 'partition'},
            search_fields=['code__icontains', 'description__icontains'],
        ),
        required=False,
        label=_("Alarm Code")
    )
    
    
    zone = forms.ModelChoiceField(
        queryset=Zone.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=Zone,
            dependent_fields={'account': 'account', 'partition': 'partition'},
            search_fields=['code__icontains', 'name__icontains'],
        ),
        required=False,
        label=_("Zone")
    )
        
    user = forms.ModelChoiceField(
        queryset=AccountUser.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=AccountUser,
            dependent_fields={'account': 'account', 'partition': 'partition'},
            search_fields=['code__icontains', 'name__icontains'],
        ),
        required=False,
        label=_("Account User")
    )
    
    
    created_at = forms.DateTimeField(required=True, widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}), label=_("Created At"))
      
    class Meta:
        model = DecryptedEvent
        fields = '__all__'
        
    def __init__(self, details=False, account_id=-1, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Event'),
                    Row(
                        Column('account'),
                    ),
                    Row(
                        Column('raw_event', css_class="col-1"),
                        Column('protocole', css_class="col-1"),
                        Column('receiveer_no', css_class="col-1"),
                        Column('line_no', css_class="col-1"),
                        Column('created_at', css_class='col-2'),
                        Column('partition', css_class='clo-2'),
                        Column('zone', css_class='col-2'),
                        Column('user', css_class='col-2'),              
                    ),
                    Row(
                        Column(
                            Row(
                                Column('alarm_code')
                            ),
                            Row(
                                Column('has_return')
                            ),
                            Row(
                                Column('delayed_return')
                            ),
                            Row(
                                Column('handled_return_delay')
                            ),
                            Row(
                                Column('is_last_periodic_event')
                            ),
                            Row(
                                Column('delayed_periodic')
                            ),
                            Row(
                                Column('handled_periodic_delay')
                            ),
                            Row(
                                Column('is_out_of_schedule')
                            ),
                            Row(
                                Column('is_user_out_of_schedule')
                            ),
                            Row(
                                Column('is_user_holiday')
                            ),
                            Row(
                                Column('handled_out_of_schedule')
                            ),
                            css_class="col-3"
                        ),
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
            self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(self.data['account']), label=_("Partition"))
        else:
            self.fields['partition'] = forms.ChoiceField(choices=get_partitions_choices(account_id), label=_("Partition"))
            
        if 'raw_event' in self.data and self.fields['raw_event'] == -1:
            self.fields['created_at'].disabled = True
            self.fields['partition'].disabled = True
            

        if not details:
            self.helper.add_input(Submit('submit', _('Submit'), css_class='btn-primary'))

            self.fields['protocole'].disabled = True
            self.fields['receiveer_no'].disabled = True
            self.fields['line_no'].disabled = True
            self.fields['raw_event'].disabled = True
            self.fields['has_return'].disabled = True
            self.fields['delayed_return'].disabled = True
            self.fields['is_last_periodic_event'].disabled = True
            self.fields['delayed_periodic'].disabled = True
            self.fields['is_out_of_schedule'].disabled = True
            self.fields['is_user_out_of_schedule'].disabled = True
            self.fields['is_user_holiday'].disabled = True

            if 'raw_event' in self.data and self.data['raw_event'] != -1:
                self.fields['created_at'].disabled = True

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
               