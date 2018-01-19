from django.db import models

# Create your models here.

class Person(models.Model):
	SHIRT_SIZES = (
			('S', 'Small'),
			('M', 'Medium'),
			('L', 'Large')
		)
	name = models.CharField(max_length = 60)		
	shirt_size = models.CharField(max_length = 1, 
								  choices = SHIRT_SIZES)

	#class Meta:
	#	db_table = 'Pessoa'

class Manufacter(models.Model):
	name = models.CharField(max_length = 50)


class Car(models.Model)	:
	name = models.CharField(max_length = 50)
	manufacter = models.ForeignKey(Manufacter, 
								   on_delete = models.CASCADE,
								   related_name = 'cars')


	
class Cobertura(models.Model)	:
	nome = models.CharField(max_length = 30)
	def __str__(self):
		return self.nome

class Pizza(models.Model):
	nome = models.CharField(max_length = 30)
	coberturas = models.ManyToManyField(Cobertura)

	def __str__(self):
		return self.nome

class CPF(models.Model):
	numero = models.CharField(max_length = 11)

class Pessoa(models.Model):
	nome = models.CharField(max_length = 50)
	cpf = models.OneToOneField(CPF, 
							   related_name = 'pessoa',
							   on_delete = models.CASCADE)

	def __str__(self):
		return self.nome

