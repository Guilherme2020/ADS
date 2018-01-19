from django.db import models

# Create your models here.

class Perfil(models.Model):
    '''
	def __init__(self, nome = '', email = '',
				 telefone = '', nome_empresa = ''):
		self.nome = nome
		self.email = email
		self.telefone = telefone
		self.nomelse_empresa = nome_empresa
    '''
    nome = models.CharField(max_length=255, null=False)

    telefone = models.CharField(max_length=15, null= False)

    email = models.CharField(max_length=255, null=False)

    nome_empresa = models.CharField(max_length=255, null=False)

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self,convidado = perfil_convidado)
        convite.save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='convites_feitos' )
    convidado = models.ForeignKey(Perfil, on_delete= models.CASCADE, related_name='convites_recebidos')