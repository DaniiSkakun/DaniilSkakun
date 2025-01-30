from .models import EntertainmentCenter, CenterType, Visitor, Event
from django import forms


class EntertainmentCenterForm(forms.ModelForm):
    class Meta:
        model = EntertainmentCenter
        fields = ['name', 'description', 'address', 'center_type']  # Поля форми
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  
            'description': forms.Textarea(attrs={'class': 'form-control'}), 
            'address': forms.TextInput(attrs={'class': 'form-control'}),  # Поле для введення адреси
            'center_type': forms.Select(attrs={'class': 'form-select'}),  
        }

class CenterTypeForm(forms.ModelForm):
    class Meta:
        model = CenterType
        fields = ['name', 'description']  # Поля форми
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Поле назви
            'description': forms.Textarea(attrs={'class': 'form-control'}),  # Поле для опису
        }

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['username', 'email']  # Поля форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Динамічне заповнення списку центрів при створенні відвідувача
        self.fields['center_id'].queryset = EntertainmentCenter.objects.all()

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'entertainment_center', 'description']  # Поля форми
