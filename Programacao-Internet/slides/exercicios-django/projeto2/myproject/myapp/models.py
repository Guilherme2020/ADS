from concurrent.futures import thread

from django.db import models


# Create your models here.


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField(max_length=60, null=True, default='leandro')
    # last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, null=True)


class Group(models.Model):
    name = models.CharField(max_length=60)
    members = models.ManyToManyField(Person, through='Membership', through_fields=('group', 'member'), )

    def __str__(self):
        return self.name


class Membership(models.Model):
    member = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    inviter = models.ForeignKey(Person, on_delete=models.CASCADE,
                                related_name='membership_invites')
    date_joined = models.DateField(null=True)
    invite_reason = models.CharField(max_length=64)


class Manufacter(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacter = models.ForeignKey(
        Manufacter, on_delete=models.CASCADE, related_name='cars'
    )


class Cobertura(models.Model):
    nome = models.CharField(max_length=30)


class Pizza(models.Model):
    nome = models.CharField(max_length=30)
    coberturas = models.ManyToManyField(Cobertura)

    def __str__(self):
        return self.nome


class PessoaFisica(models.Model):
    pass


class Blog(models.Model):
    name = models.CharField(max_length=50)


class Entry(models.Model):
    headline = models.CharField(max_length=60)
    body_text = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Usuario(models.Model):
    email = models.EmailField(15)
    senha = models.CharField(30)
    data_nascimento = models.DateField()


class Pefil(models.Model):
    nome = models.CharField(max_length=30)
    usuario = models.ForeignKey('Perfil', on_delete=models.CASCADE)
    pedidos_amizade = models.ManyToManyField('Perfil', through='Convite')

class Convite(models.Model):
    data = models.DateField()
    STATUS_CONVITE = (
        ('PENDENTE','pendente'),
        ('ACEITO', 'aceito'),
        ('RECUSADO', 'recusado')
    )
    aceito  = models.CharField(choices=STATUS_CONVITE, max_length=20, default=STATUS_CONVITE[0][0])
    solicitante = models.ForeignKey('Perfil', on_delete=models.CASCADE)
    solicitado = models.ForeignKey('Perfil',on_delete=models.CASCADE)

class Postagem(models.Model):

    texto = models.TextField()
    data_postagem = models.DateTimeField()
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='postagem')

class Comentario(models.Model):

    texto = models.TextField()
    data = models.DateField()
    perfil = models.ForeignKey('Perfil',on_delete=models.CASCADE,related_name='comentarios')
    postagem = models.ForeignKey('Postagem',on_delete=models.CASCADE,related_name='comentarios')
    respostas = models.ForeignKey('Comentario',on_delete=models.CASCADE)

class Amizade(models.Model):
    pass

class Reacao(models.Model):
    TIPO_REACAO = (
        ('CURTIR', 'curtir'),
        ('AMAR', 'amar'),
        ('RIR', 'rir'),
        ('UAL', 'ual'),
        ('TRISTE','triste'),
        ('IRRITADO','irritado')

    )
    tipo = models.CharField(choices=TIPO_REACAO, default=TIPO_REACAO[0][1])
    data = models.DateField()
    perfil = models.ForeignKey('Perfil',on_delete=models.CASCADE, related_name='pefis')
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='postagens')
    peso = models.IntegerField()


from myapp.models import *


def script():
    user = Usuario(email = 'gui@gmail.com',senha = '21212121',dt_nascimento = '2015-05-12')
    user.save()
    user2 = Usuario(email="gui@gmail.com", senha="21212121", dt_nascimento="2015-05-12")

    perfil = Perfil(nome = 'alguuem', usuario = user)
    perfil2 = Perfil(nome = 'alguem2',usuario = user2)

    Usuario.objects.get()
    Usuario.objects.all()

    post1 = Postagem()

'''
>>> from myapp.models import *
>>> p = Pizza(nome = 'Calabresa')
>>> c1 = Cobertura(descricao = 'Molho de tomate')
>>> c2 = Cobertura(descricao = 'Mozarela')
>>> c3 = Cobertura(descricao = 'Linguica calabresa')
>>> coberturas = [c1,c2,c3]
>>> p.save()
>>> c1.save()
>>> c2.save()
>>> c3.save()
>>> coberturas = [c1,c2,c3]
>>> p.coberturas = coberturas
>>> p.save()
>>> p1 = Pizza.objects.get(id = 1)
>>> p1.coberturas.all()
'''
