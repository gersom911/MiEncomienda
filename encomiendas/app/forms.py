from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import TrabajaConNosotro,Encomienda, Conductor
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']
    
    
class ContactoForms(ModelForm):
    nombre = forms.CharField(min_length=10)
    
    class Meta():
        model = TrabajaConNosotro
        
        fields = '__all__'
        
        
class EstadoConductorForms(ModelForm):
   
    
    class Meta():
        model = Conductor
        
        fields =['estado_trabajador', ] 
        
        

        
class EncomiendaModificarForms(ModelForm):
    class Meta():
        model = Encomienda
        fields = ['estado', ]

class EncomiendaForms(ModelForm):
    class Meta():
        model = Encomienda
        fields = ['numero_usuario', 'nombre' ,'ruta', 'nombre_envia','telefono_envia','direccion_salida', 'punto_referencia_salida',
                  'nombre_recibe' ,'telefono_recibe', 'dirección_llegada' ,  'punto_referencia_llegada' , 'conductor',
                  ]

class EncomiendaForms(ModelForm):
    class Meta():
        model = Encomienda
        fields = ['numero_usuario', 'nombre' ,'ruta', 'nombre_envia','telefono_envia','direccion_salida', 'punto_referencia_salida',
                  'nombre_recibe' ,'telefono_recibe', 'dirección_llegada' ,  'punto_referencia_llegada' , 'conductor',
                  ]

class EvaluarConductorForms(ModelForm):
    class Meta():
        model = Encomienda
        fields = ['evaluacion','descripcion_evaluacion',
                  ]
        
    
        
        
        