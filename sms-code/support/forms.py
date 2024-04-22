

from django import forms
from extra_views import InlineFormSetFactory

from accounts.models import Account
from support.models import ServiceOrder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column
from django_select2 import forms as s2forms


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
        fields = ('account', 'status' , 'summary', 'request', 'internal_notes', 'closed_at', )
        
    def __init__(self, details=False, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        
        self.helper = FormHelper()

        if not details:
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        else:            
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
        kwargs['form_kwargs']['details'] = True
                
        return kwargs