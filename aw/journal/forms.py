from django import forms
from . import models
from .widgets import FengyuanChenDatePickerInput

class JournalForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%m/%d/%Y'], widget=FengyuanChenDatePickerInput())
    class Meta:
        fields = ("date", "user", "river", "flow", "description", "public")
        model = models.JournalEntry
