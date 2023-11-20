from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["birth_date", "mobile_number"]
        widgets = {
            "birth_date": forms.DateInput(
                attrs={"class": "form-control form-control-lg", "type": "date"}
            ),
            "mobile_number": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Mobile Number",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Additional initialization logic can go here if needed

    def clean(self):
        cleaned_data = super().clean()
        birth_date = cleaned_data.get("birth_date")
        mobile_number = cleaned_data.get("mobile_number")

        # You can add additional validation or processing here if necessary

        return cleaned_data
