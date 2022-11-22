
from django.urls import path
from .views import registro,interno,index, TrabajaConNosotro,evaluacion,precio,miEncomienda,plataformaInicio,conductor,miEncargo
from .views import detalle, encomiendaModificar,detalleCliente,nuevaEncomienda,evaluarConductor,estadoCondutor
urlpatterns = [
    #rutas de interiores
    path('interno/',  interno, name = 'interno'),
    path('evaluacion/<int:id>/',  evaluacion, name = 'evaluacion'),
    path('precio/',  precio, name = 'precio'),
    path('plataforma_Inicio/', plataformaInicio, name = 'plataforma_Inicio'),
    path('conductor/', conductor, name = 'conductor'),
    path('mis_encargos/<int:id>/', miEncargo, name = 'miencargo'),
    path('detalles/<int:id>/', detalle, name = 'detalles'),
    path('detalles_cliente/<int:id>/', detalleCliente, name = 'detalles_cliente'),
    path('modificar_estado/<int:id>/',encomiendaModificar, name = 'modificar_estado'),
    path('mis_encomiendas/<int:id>/',  miEncomienda, name = 'miencomienda'),
    path('nueva_encomienda/',  nuevaEncomienda, name = 'nuevaencomienda'),
    path('evaluar_conductor/<int:id>/',  evaluarConductor, name = 'evaluarconductor'),
    path('miestado/<int:id>/',  estadoCondutor, name = 'miestado'),
    # rutas exteriores
    path('',  index, name = 'index'),
    path('registro/',  registro, name = 'registro'),
    path('trabaja/',  TrabajaConNosotro, name = 'trabaja'),
    
    
    
]