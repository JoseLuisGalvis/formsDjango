from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        # fields = '__all__' Para Mostrar Todos los Campos
        fields = ['name', 'email', 'message', 'contact_type', 'subscription']
        # help_text = {''}
    
    
    
    
    
    
    
    
    """ name = forms.CharField(label='Nombre y Apellido', required=True, min_length=5, max_length=35, widget=forms.TextInput(attrs=
    {'class':'form-control', 'placeholder': 'Introduzca sus Datos'}))
    email = forms.EmailField(label='Correo Electrónico', required=True, max_length=100, widget=forms.EmailInput(attrs=
    {'class':'form-control', 'placeholder': 'Introduzca su email'}))
    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs=
    {'class':'form-control', 'placeholder': 'Esciba Aquí su Mensaje.....', 'rows': 7}))
    """
   
