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


class MaintenanceSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255, required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search for maintenance"
            }
        )
    )

