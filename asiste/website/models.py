from django.db import models

class Programa(models.Model):
  id_programa = models.IntegerField(primary_key=True, max_length=30)
  nombre_programa = models.CharField(max_length=50)
  version_programa = models.CharField(max_length=45)
  coordinacion = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre_programa

class Ficha(models.Model):
  id_ficha = models.IntegerField(max_length=15, primary_key=True)
  id_programa = models.ForeignKey(Programa, on_delete=models.PROTECT)
  nombre_programa = models.CharField(max_length=45)

  def __str__(self):
    return self.nombre_programa

class Instructor(models.Model):
  documento_instructor = models.IntegerField(max_length=30, primary_key=True)
  nombres_instructor = models.CharField(max_length=100)
  apellidos_instructor = models.CharField(max_length=100)
  correo_misena_instructor = models.EmailField(max_length=100)
  id_ficha_instructor = models.ForeignKey(Ficha, on_delete=models.PROTECT)

  def __str__(self):
    return f"{self.nombres_instructor} {self.apellidos_instructor}"

class Aprendiz(models.Model):
  documento_aprendiz = models.IntegerField(max_length=30, primary_key=True)
  nombres_aprendiz = models.CharField(max_length=45)
  apellidos_aprendiz = models.CharField(max_length=45)
  correo_personal_aprendiz = models.EmailField(max_length=100)
  correo_institucional_aprendiz = models.EmailField(max_length=100)
  ficha_aprendiz = models.ForeignKey(Ficha, on_delete=models.PROTECT)
  celular_aprendiz = models.IntegerField(max_length=10)
  estado_asitencia_aprendiz = models.BooleanField(default=False)
  time_aprendiz = models.DateTimeField(auto_now=True)
  def __str__(self):
    return f"{self.nombres_aprendiz} {self.apellidos_aprendiz}"
