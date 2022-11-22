from django.shortcuts import render
from .forms import CustomUserCreationForm,EncomiendaModificarForms,EncomiendaForms,EvaluarConductorForms,EstadoConductorForms,ContactoForms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from .forms import ContactoForms
from .models  import Conductor,Evaluacion,Precio,Encomienda

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# esta vista controla el registro de las personas a el app

#--------------------------------
#----- Registro ------------------
#--------------------------------

def registro(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user)
            messages.success(request, 'Se ha registrado correctamente')
            return redirect(to='index') 

        else:
            data['form'] = formulario  

    return render(request,  'registration/registro.html', data)


#--------------------------------
#----- Interno ------------------
#--------------------------------

def interno(request):
    conductor = Conductor.objects.filter(estado_trabajador='TA').order_by('nombre')
    dato = {'entity':conductor
              }
    return render(request,  'app/interno.html',dato)

#--------------------------------
#----- plataformainicio ------------------
#--------------------------------
@login_required
def plataformaInicio(request):
    
    if request.user.groups.filter(name='conductor').exists():
        return redirect(to='conductor')
    
    else:
        return redirect(to='interno')
    
    return render(request, 'app/plataforma_inicio.html')



#--------------------------------
#----- conductor ------------------
#--------------------------------

def conductor(request):
    conductor = Conductor.objects.filter(estado_trabajador='TA').order_by('nombre')
    dato = {'entity':conductor
              }
       
    return render(request,  'app/conductor.html',dato)



#--------------------------------
#----- MIs encargos ------------------
#--------------------------------

def miEncargo(request,id):
    conducto = Conductor.objects.filter(username=id)
    colicionador = 0
    for i in conducto:
        colicionador = i.colicionador
    
    
    encomienda = Encomienda.objects.filter(conductor=colicionador).order_by('fecha_entrega')
    
    
    dato = {'entity':encomienda
              }
       
    return render(request,  'app/mis_encargos.html',dato)


#--------------------------------
#----- Evaluacionn --------------
#--------------------------------


def evaluacion(request,id):
    evaluacion = Encomienda.objects.filter(conductor =id).order_by('conductor')
   

    data = {'entity':evaluacion,
             }
   

    return render(request, 'app/evaluacion.html',data)



#--------------------------------
#----- precio --------------
#--------------------------------


def precio(request):
    precio = Precio.objects.all().order_by('precio')
   

    data = {'entity':precio,
             } 
   

    return render(request, 'app/precio.html',data)


#--------------------------------
#----- Index ------------------
#--------------------------------

def index(request):
    

    return render(request,  'app/index.html',{})

def trabaja(request):
    

    return render(request,  'app/trabaja.html',{})

#--------------------------------
#----- Trabajja con nosotrios ------------------
#--------------------------------


def TrabajaConNosotro(request):
    
    data = {'form':ContactoForms()}
    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST) 
        if formulario.is_valid():
            formulario.save()
            messages.success(request,f"has iniciado el proceso, nos estaremos comunicando contigo")
            return redirect(to='index')
        else:
            data['form'] = formulario#sino es correcto le reenvio el formulario al usuario.
   
    return render(request,  'app/trabaja.html',data)   


#--------------------------------
#----- mis encomiendas --------------
#--------------------------------


def miEncomienda(request,id):
    encomienda = Encomienda.objects.filter(numero_usuario= id).order_by('fecha_entrega')
   

    data = {'entity':encomienda,
             }
   

    return render(request, 'app/mis_encomienda.html',data)



#--------------------------------
#----- detalle --------------
#--------------------------------


def detalle(request,id):
    detalle = Encomienda.objects.filter(id=id)
   

    data = {'entity':detalle,
             }
   

    return render(request, 'app/detalles.html',data)


#--------------------------------
#----- detalle --------------
#--------------------------------


def detalleCliente(request,id):
    detalle = Encomienda.objects.filter(id=id)
   

    data = {'entity':detalle,
             }
   

    return render(request, 'app/detalles_cliente.html',data)


#--------------------------------
#----- ModificarEstado --------------
#--------------------------------



def encomiendaModificar(request,id):
    encomienda = get_object_or_404(Encomienda, id=id)
    data = {'form': EncomiendaModificarForms(instance=encomienda)}
    if request.method == 'POST':
        formulario = EncomiendaModificarForms(data=request.POST,instance=encomienda )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'encomienda modificada')
            return redirect(to='plataforma_Inicio')
            
        else:
            data['form'] = formulario

    return render(request, 'app/modificar_estado.html',data)

#--------------------------------
#----- NUeva encomienda--------------
#--------------------------------
def nuevaEncomienda(request):
    data = {'form':EncomiendaForms()}
    if request.method == 'POST':
        formulario = EncomiendaForms(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'encomienda  asignada')
            return redirect(to='plataforma_Inicio')
            
        else:
            data['form'] = formulario
    return render(request,  'app/nueva_encomienda.html',data)

#--------------------------------
#----- ModificarEstado --------------
#--------------------------------



def evaluarConductor(request,id):
    encomienda = get_object_or_404(Encomienda, id=id)
    data = {'form': EvaluarConductorForms(instance=encomienda)}
    if request.method == 'POST':
        formulario = EvaluarConductorForms(data=request.POST,instance=encomienda )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Gracias por tu opinión')
            return redirect(to='plataforma_Inicio')
            
        else:
            data['form'] = formulario

    return render(request, 'app/evaluar_conductor.html',data)

#--------------------------------
#----- EstadoConductor --------------
#--------------------------------



def estadoCondutor(request,id):
    conductor = get_object_or_404(Conductor, username=id)
    data = {'form': EstadoConductorForms(instance=conductor)}
    if request.method == 'POST':
        formulario = EstadoConductorForms(data=request.POST,instance=conductor )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'su estdo ha sido modificado')
            return redirect(to='plataforma_Inicio')
            
        else:
            data['form'] = formulario

    return render(request, 'app/mi_estado.html',data)