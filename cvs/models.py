from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    sobre_mi =  models.CharField(max_length=300)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    likedin = models.CharField(max_length=200)

    pub_date = models.DateTimeField("Fecha update")
    
    def __str__(self):
        return self.nombre + " "+self.apellidos

class Experiencia(models.Model):
    experiencia = models.ForeignKey(Persona, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=200)
    ubicacion= models.CharField(max_length=100)
    puesto = models.CharField(max_length=200)
    descripcion= models.CharField(max_length=400, default='')

    inicio_date = models.DateField("inicio trabajo")
    final_date = models.DateTimeField("final trabajo")

    anios = models.IntegerField(default=0)

    def __str__(self):
        return self.puesto + "/" + self.empresa
    
    class Habilidad(models.Model):
     habilidad = models.ForeignKey(Persona, on_delete=models.CASCADE)
     especialidad = models.CharField(max_length=100)
     porcentajes= models.CharField(default=50)
  

    def __str__(self):
        return self.especialidad + ".Porcentaje (" + self.porcentaje + "%)"
    
    class Idioma(models.Model):
   
     IDIOMAS = {
        "ES": "Español",
        "EN": "Ingles",
        "FR": "Frances",
        "DE": "Alemán"
        }
     
     
     NIVEL = {
        "A1" : "A1",
        "A2": "A2",
        "B1": "B1",
        "B2" : "B2",
        "C1": "C1",
        "C2" : "C2"

     }
     
     idioma = models.ForeignKey(Persona, on_delete=models.CASCADE)
     lenguaje= models.CharField(max_length=2, choices=IDIOMAS)
     nivel= models.CharField(max_length=2, choices=NIVEL)
  

    def __str__(self):
        return self.lenguaje+ ".Nivel:" + self.nivel 
    
    class Interes(models.Model):
      interes = models.ForeignKey(Persona, on_delete=models.CASCADE)
      especialidad = models.CharField(max_length=100)
    

    def __str__(self):
        return self.mi_interes
    
class Educacion(models.Model):
    educacion = models.ForeignKey(Persona, on_delete=models.CASCADE)
    escuela = models.CharField(max_length=200)
    ubicacion= models.CharField(max_length=100)
    estudio = models.CharField(max_length=200)

    final_date = models.DateTimeField("fecha de finalización")



    def __str__(self):
        return self.estudio + ". " + self.escuela + "("+self.final_date+")"
    
# Create your models here.
