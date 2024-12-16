from django import forms
from . models import Appointment
from django.forms import TextInput, Textarea

class AppointmentFrom(forms.ModelForm):
    class Meta:
        model=Appointment
        fields= ['name','email','child_name','child_age','message']
        widgets={
            'name': TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "id":"gname",
                "placeholder":"Gurdian Name"
            }),
            'email': TextInput(attrs={
                "type":"email",
                "class":"form-control border-0",
                "id":"gmail",
                "placeholder":"Gurdian Email"
            }),
            'child_name':TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "id":"cname",
                "placeholder":"Child Name"
            }),
            'child_age': TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "id":"cage",
                "placeholder":"Child Age"
            }),
            'message': Textarea(attrs={
                "class":"form-control border-0",
                "placeholder":"Leave a message here",
                "id":"message",
                "style":"height: 100px"
            })
        }

        