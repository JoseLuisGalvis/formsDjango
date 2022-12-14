from django.db import models

# Create your models here.

options =[
    [0, 'Pedido de Información'],
    [1, 'Queja por Producto'], 
    [2, 'Felicitaciones']
]

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre y Apellido')
    email = models.EmailField(verbose_name='Correo Electrónico')
    message = models.TextField(verbose_name='Mensaje')
    contact_type = models.IntegerField(choices=options, verbose_name='Tipo de Contacto')
    subscription = models.BooleanField(default=False, verbose_name='Suscribirme a Correos Informativos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Envío') 
    