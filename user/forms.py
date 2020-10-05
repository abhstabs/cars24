from django import forms

REGION_CHOICES = (("ABC","ABC"), ("DEF","DEF"),("EFG","EFG"))

class DateInput(forms.DateInput):
    input_type = 'date'

class SampleForm(forms.Form):
    email = forms.EmailField(required=True)
    region = forms.ChoiceField(choices = REGION_CHOICES, required=True)
    branch_name = forms.CharField(label='Branch Name', required=True)
    ra_email_id = forms.ChoiceField(choices=REGION_CHOICES, label='RA Email Id', required=True)
    appointment_id = forms.CharField(required=True)
    first_inspection_date = forms.DateField(required=True, widget=DateInput())
    # calls_made = forms.CheckBoxSelectMultiple(choices=RAEGION_CHOICES)
    type_of_lead = forms.RadioSelect(choices=REGION_CHOICES)


