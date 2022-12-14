from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm # Importamos el Formulario Creado
from django.core.mail import EmailMessage 

def contact(request):
    contact_form = ContactForm() # Inicializar el Formulario 
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            
            email = EmailMessage(
                'Su Contraseña ha sido Actualizada',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name, email, message),
                email,
                ['desarrollo@findergreenenergy.com'],
                reply_to=['email'],
            )
            
            try:
                email.send()
                # Está Todo OK
                return redirect(reverse('contact') + '?ok')
            except:
                # Ha Habido un Error y retorno a Error
                return redirect(reverse('contact') + '?error')
        
    return render(request, 'contact/contact.html', {'form': contact_form}) #Agregamos diccionario de contexto


        
