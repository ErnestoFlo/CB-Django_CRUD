from django import forms
from .models import crud

class crudForm(forms.ModelForm):
    class Meta:
        model = crud
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
