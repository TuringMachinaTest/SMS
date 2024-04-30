

from django import forms
from extra_views import InlineFormSetFactory

from accounts.models import Account
from support.models import ServiceOrder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column
from django_select2 import forms as s2forms
from crispy_formset_modal.layout import ModalEditLayout, ModalEditFormsetLayout
from django.utils.translation import gettext as _


class ServiceOrderForm(forms.ModelForm):

    account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=Account,
            search_fields=['id__icontains', 'name__icontains'],
        )
    )
    
    closed_at = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    
    class Meta:
        model = ServiceOrder
        fields = '__all__'
        
    def __init__(self, details=False, formset=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column("account"),
            ),
            Row(
                Column("status"),
            ),
            Row(
                Column("summary"),
            ),
            Row(
                Column("request"),
            ),
            Row(
                Column("internal_notes"),
            ),
            Row(
                Column("response"),
            ),
            Row(
                Column("closed_at"),
            ),
        )

        self.fields["closed_at"].disabled = True

        if not details and not formset:
            self.helper.add_input(Submit('submit', _('Submit'), css_class='btn-primary'))
        elif details:            
            for field in self.fields:
                self.fields[field].disabled = True   


class ServiceOrderInlineFormSet(InlineFormSetFactory):
   
    model = ServiceOrder
    form_class = ServiceOrderForm
    factory_kwargs = {"extra": 0}
    
    def get_formset_kwargs(self):
        kwargs = super(ServiceOrderInlineFormSet, self).get_formset_kwargs()

        #self.formset_kwargs = { 'form_kwargs' : { 'account_id' : kwargs['instance'].id}}
        # Add any additional parameters you want to pass to the form
        #print(kwargs)
        
        kwargs['form_kwargs'] = {}
        kwargs['form_kwargs']['details'] = False
        kwargs['form_kwargs']['formset'] = True

                
        return kwargs