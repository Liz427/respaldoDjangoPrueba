from django.db import models

class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12, verbose_name='Matrícula') #Texto corto | Con verbose_name renombramos el campo
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['-created']
        #el menos indica que se ordenará del más reciente al más viejo

    def __str__(self):
        return self.nombre