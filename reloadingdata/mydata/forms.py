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
        fields = ( 'bullet', 'powder', 'primer' ,'coal' ,'landTotal' ,'landOffset')

        widgets ={
            
            'bullet': forms.TextInput(attrs={'class': 'form-control'}),
            'powder': forms.TextInput(attrs={'class': 'form-control'}),
            'primer': forms.TextInput(attrs={'class': 'form-control'}),
            'coal': forms.NumberInput(attrs={'class': 'form-control'}),
            'landTotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'landOffset': forms.NumberInput(attrs={'class': 'form-control'}),
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