from django.contrib import admin
from .models import Evaluacion, LugarNacimiento,Lugar_llegada,Lugar_salida, Vehiculo,Conductor,Ruta,Precio,Estado,Encomienda,Volumen,TipoMaterial,Peso

@admin.register(LugarNacimiento)
class ContactoAdmin(admin.ModelAdmin):
    pass
   # list_display =  ( 'nombre','tipo_consulta ','mensaje','correo')#coloca esto en el admin los campos
    #ordering =['-nombre',] #ordena edescendete por nombre
    #search_fields = ['nombre'] #sirve para las busquedas en eladmin
    #list_display_links = ('texto_pequenio',) #permite editar el campo que se marque
    #list_editable =('nombre',) #edita los campos en el genral
    #list_filter = ('texto_pequenio',)
    #list_per_page = 3 #ganina los resultados
    
@admin.register(Lugar_llegada)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Lugar_salida)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehiculo)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Conductor)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Ruta)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Precio)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Estado)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Encomienda)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Evaluacion)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Peso)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Volumen)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoMaterial)
class ContactoAdmin(admin.ModelAdmin):
    pass

