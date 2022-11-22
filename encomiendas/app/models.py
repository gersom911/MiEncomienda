from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

#--------------------------------
#----- Lugar de Nacimiento------
#-------------------------------
class LugarNacimiento(models.Model):
     ciudad = models.CharField(max_length=100, verbose_name ='Lugar de nacimiento')
     departamento = models.CharField(max_length=100, verbose_name ='Estado/Departamento')
     pais = models.CharField(max_length=100, null = True, verbose_name ='Pais')
    
          
    
     def __str__(self):
        return self.ciudad



#--------------------------------
#----- Vehículo------------------
#-------------------------------
class Vehiculo(models.Model):
    marca = models.CharField(max_length=10, null =True,blank = True, verbose_name ='marca')
    placa = models.CharField(max_length=10, null =True,blank = True, verbose_name ='Placa ')
    bicicleta = 'Bicicleta'
    moto  = 'Moto'
    sedan = 'Sedan'
    camioneta  = 'Camioneta'
    camion  = 'Camión'

    
    TIPO_VEHICULO  = [
        (bicicleta , 'Bicicleta'),
        (moto, 'Moto'),
        (sedan, 'Sedan'),
        (camioneta, 'Camioneta'),
        (camion , 'Camión'),
        
    ]
              
    tipo_vehiculo = models.CharField(
        max_length=50,
        choices= TIPO_VEHICULO,
        verbose_name ='Tipo de vehiculo'
       
    )
    anio = models.DateField( verbose_name ='escriba la fecha de compra del vehículo')
    placa = models.CharField(max_length=10, null =True,blank = True, verbose_name ='Placa ')
    
     
    def __str__(self):
          return self.tipo_vehiculo
     
    
#--------------------------------
#----- Conductor------------------
#--------------------------------

class Conductor(models.Model):
    username =  models.ForeignKey(User,null = True, on_delete=models.CASCADE, verbose_name ='mi usuario')
    nombre= models.CharField(max_length=100, verbose_name ='Nombre del conductor')
    colicionador = models.IntegerField(null =True,blank = True,verbose_name ='colicionador')
   
    vehiculo = models.OneToOneField(
        Vehiculo,
        on_delete=models.CASCADE,
        primary_key=True)
    foto = models.ImageField(upload_to = "foto", null =True,blank = True) 
    foto_vehiculo = models.ImageField(upload_to = "foto_vehiculo",  null =True,blank = True)
    username = models.ForeignKey(User,null = True, on_delete=models.CASCADE, verbose_name ='Usuario')
    numero_identidad = models.CharField(max_length=100, verbose_name ='Número de documento de identidad')
    telefono = models.CharField(max_length=50,  null =True,blank = True, verbose_name ='Teléfono local')
    celular =  models.CharField(max_length=50, null =True,blank = True, verbose_name ='Celular')
    email =  models.EmailField(max_length=254, null =True,blank = True, verbose_name ='Correo')
    direccion =  models.CharField(max_length=50,  null =True,blank = True,verbose_name ='Dirección')
     
    Soltero= 'SO'
    Casado = 'CA'
    Union_hecho= 'UH'
    
    ESTADO_CIVIL = [
        (Soltero, 'Soltero'),
        (Casado, 'Casado'),
        (Union_hecho, 'Union de hecho'),
        
    ]
    estado_civil = models.CharField(
        max_length=2,
        choices=ESTADO_CIVIL,
        default=Casado,verbose_name ='Estado Civil'
    )
     
    Masculino= 'M'
    Femenino = 'F'
        
    SEXO = [
        (Masculino, 'Masculino'),
        (Femenino, 'Femenino'),
                
    ]
    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
        verbose_name ='Sexo'
    )
     
    ciudad_nacimiento = models.ForeignKey(LugarNacimiento, on_delete=models.CASCADE, verbose_name ='Lugar de nacimiento')
    fecha_nacimiento = models.DateField( verbose_name ='Fecha de nacimiento')
    
    
    
    trabajando= 'TA'
    descansando = 'DE'
    
    
    ESTADO_TRABAJO = [
        (trabajando, 'Trabajando'),
        (descansando, 'Descanso')
            
    ]
    estado_trabajador = models.CharField(
        max_length=2,
        choices=ESTADO_TRABAJO,
        default=descansando,verbose_name ='Estado del conductor'
    )
    def __str__(self):
        return self.nombre
  
 #--------------------------------
#----- EVALUACION------------------


#--------------------------------

class Evaluacion(models.Model):
    comentario = models.CharField(max_length=150, null =True,blank = True, verbose_name ='evaluación ')
    malo = 'Malo'
    regular  = 'Regular'
    bueno = 'Bueno'
    excelente  = 'Excelente'
    

    
    EVALUACION  = [
        (malo , 'malo'),
        (regular, 'regular'),
        (bueno, 'bueno'),
        (excelente, 'excelente')
       
        
    ]
                  
    evaluacion = models.CharField(
        max_length=50,
        choices= EVALUACION,
        verbose_name ='Tipo de vehiculo'
       
    )
    
    conductor= models.ForeignKey(Conductor, on_delete=models.CASCADE, null =True,blank = True,verbose_name ='conductor')
    def __str__(self):
        return self.evaluacion

#--------------------------------
#----- Lugares-----------------
#-------------------------------
class Lugar_salida(models.Model):
     lugar = models.CharField(max_length=100, verbose_name ='Lugar de la ciudad')
    
     def __str__(self):
        return self.lugar
    
#--------------------------------
#----- Lugares-----------------
#-------------------------------
class Lugar_llegada(models.Model):
     lugar = models.CharField(max_length=100, verbose_name ='Lugar de la ciudad')
    
     def __str__(self):
        return self.lugar

#--------------------------------
#----- rutas-----------------
#-------------------------------
class Ruta(models.Model):
    ruta =  models.CharField(max_length=100, verbose_name ='Ruta')
    
    desde = models.ForeignKey(Lugar_salida, on_delete=models.CASCADE,  null =True,blank = True,verbose_name ='lugar referencial de salida')
    hasta = models.ForeignKey(Lugar_llegada, on_delete=models.CASCADE,  null =True,blank = True,verbose_name ='lugar referencial de llegada')
    
    def __str__(self):
        return self.ruta
 #--------------------------------
#----- peso-----------------
#-----------------------------  
class Peso(models.Model):
    peso =  models.CharField(max_length=100,  null =True,blank = True,verbose_name ='Escriba peso aproximado')
     
    def __str__(self):
        return self.peso

#--------------------------------
#----- Volumen-----------------
#-----------------------------  
class Volumen(models.Model):
    volumen = models.CharField(max_length=10,  null =True,blank = True,verbose_name ='Escriba el volumen')
    alto =  models.CharField(max_length=10,  null =True,blank = True,verbose_name ='alto')
    largo = models.CharField(max_length=10,  null =True,blank = True,verbose_name ='largo')
    
    def __str__(self):
        return self.volumen 
    
#--------------------------------
#----- TipoMatreial-----------------
#-----------------------------  
class TipoMaterial(models.Model):
    nombre = models.CharField(max_length=10, null =True,blank = True, verbose_name ='nombre del material')
    descripción =  models.CharField(max_length=100, null =True,blank = True, verbose_name ='descripcion del material')
   
    
    def __str__(self):
        return self.nombre
    
    
#--------------------------------
#----- precios-----------------
#-----------------------------
class Precio(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, null =True,blank = True, verbose_name ='ruta')
    peso = models.ForeignKey(Peso, on_delete=models.CASCADE, null =True,blank = True,verbose_name ='peso')
    volumen = models.ForeignKey(Volumen, on_delete=models.CASCADE,  null =True,blank = True,verbose_name ='volumen')
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE,  null =True,blank = True,verbose_name ='tipo de materiales')
    
        
    precio = models.IntegerField(verbose_name ='precio')
    
    def __str__(self):
        return str(self.precio)

    
#--------------------------------
#----- Estado-----------------
#----------------------------
class Estado(models.Model):
    tipo =models.CharField(max_length=15, verbose_name ='defina el estado')
    descripcion= models.CharField(max_length=15, verbose_name ='de una breve descripción del estado')
    
    def __str__(self):
        return self.tipo
   
    
#--------------------------------
#----- Encomienda-----------------
#-----------------------------


    
def validarUsuario(numero_usuario):
    if type(numero_usuario) != int:
        raise ValidationError(f'EL {numero_usuario} es invalido')
    
    return numero_usuario
    
class Encomienda(models.Model):
    username = models.ForeignKey(User,null = True, on_delete=models.CASCADE, verbose_name ='mi usuario')
    numero_usuario = models.PositiveIntegerField(null = True,validators=[validarUsuario,], verbose_name ='escriba su numero de usuario')
    nombre = models.CharField(max_length=15, verbose_name ='¿asigne un título de referencia a la encomienda?')
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, verbose_name ='ruta')
    nombre_envia = models.CharField(max_length=15, verbose_name ='¿Quién envía?')
    telefono_envia = models.CharField(max_length=15, verbose_name ='teléfono de quien envía')
    direccion_salida = models.CharField(max_length=100, verbose_name ='Dirección exacta de salida')
    punto_referencia_salida = models.CharField(max_length=100, verbose_name ='proporcione un punto de referencia de salida')
    nombre_recibe = models.CharField(max_length=15, verbose_name ='¿Quién recibe?')
    telefono_recibe = models.CharField(max_length=15, verbose_name ='teléfono de quien recibe')
    dirección_llegada = models.CharField(max_length=100, verbose_name ='Dirección exacta de llegada')
    punto_referencia_llegada = models.CharField(max_length=100, verbose_name ='proporcione un punto de referencia de  llegada')
    estado = models.ForeignKey(Estado,null = True, default =1, on_delete=models.CASCADE, verbose_name ='estado de la encomienda')
    conductor = models.ForeignKey(Conductor,null = True, on_delete=models.CASCADE, verbose_name ='elija el conductor')
    fecha_entrega= models.DateTimeField(auto_now_add=True,null = True, verbose_name ='Fecha de encargo')
    malo = 'Malo'
    regular  = 'Regular'
    bueno = 'Bueno'
    excelente  = 'Excelente'
    

    
    EVALUACION  = [
        (malo , 'malo'),
        (regular, 'regular'),
        (bueno, 'bueno'),
        (excelente, 'excelente')
       
        
    ]
    evaluacion = models.CharField(
        max_length=50,
        choices= EVALUACION,
        null =True,blank = True,
        verbose_name ='evalue al conductor'
       
    )
    
    descripcion_evaluacion = models.CharField(max_length=150, null =True,blank = True, verbose_name ='Descripción de evaluación')
    
    
    def __str__(self):
        return self.nombre
    
#--------------------------------
#----- EVALUACION------------------
#--------------------------------
class TrabajaConNosotro(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    asunto =  models.CharField(max_length=50)
    mensaje = models.TextField()
        
    def __str__(self):
        return self.nombre

