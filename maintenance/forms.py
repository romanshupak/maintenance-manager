from django import forms
from maintenance.models import Maintenance


class MaintenanceForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label='Deadline'
    )

    class Meta:
        model = Maintenance
        fields = ["name", "description", "deadline", "is_completed", "department", "person_in_charge"]
        widgets = {
            "person_in_charge": forms.CheckboxSelectMultiple,
        }
