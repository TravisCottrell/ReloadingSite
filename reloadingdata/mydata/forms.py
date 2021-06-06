from django import forms
from django import forms
from .models import Gun, Bullet, TestResult, Velocity
    
class GunForm(forms.ModelForm):
    class Meta:
        model = Gun
        fields = ('gun',)

        widgets ={
            'gun': forms.TextInput(attrs={'class': 'form-control'}),
            #'owner': forms.Select(attrs={'class': 'form-control'})
        }

class BulletForm(forms.ModelForm):
    class Meta:
        model = Bullet
        fields = ( 'bullet', 'powder')

        widgets ={
            
            'bullet': forms.TextInput(attrs={'class': 'form-control'}),
            'powder': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = ( 'charge', 'moa')

        widgets ={
            
            'charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'moa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class VelocityForm(forms.ModelForm):
    class Meta:
        model = Velocity
        fields = ( 'shotnumber', 'velocity')

        widgets ={
            
            'shotnumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'velocity': forms.NumberInput(attrs={'class': 'form-control'}),
        }