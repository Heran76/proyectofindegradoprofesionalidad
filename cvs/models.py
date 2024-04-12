from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    likedin = models.CharField(max_length=200)

    pub_date = models.DateTimeField("Fecha update")
    
    def __str__(self):
        return self.nombre + " "+self.apellidos
class Experiencia(models.Model):
    experiencia = models.ForeignKey(Persona, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=200)
    puesto = models.CharField(max_length=200)
    descripcion= models.CharField(max_length=400, default='')

    inicio_date = models.DateField("inicio trabajo")
    final_date = models.DateTimeField("final trabajo")

    anios = models.IntegerField(default=0)

    def __str__(self):
        return self.puesto + "/" + self.empresa

# Create your models here.
