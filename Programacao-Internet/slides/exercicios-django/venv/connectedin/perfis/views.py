from django.shortcuts import render

# Create your views here.
#

from django.shortcuts import render
from django.http import HttpResponse

from perfis.models import Perfil


def index(request):
    # return HttpResponse('Bem Vindo Ao connected In')
    return render(request,'index.html')
def exibir(request, perfil_id):
    perfil = Perfil()
    if(perfil_id == 1):
        perfil = Perfil('Elvis','elvis@gmail.com','99999-9999', 'IFPI')
    if perfil_id == 2:
        perfil = Perfil('Lucas', 'lucas@gmail.com',
                        '99987-4567', 'TCE')
    #print('Id do Perfil recebido %s' %(perfil_id))
    return render(request,'perfil.html',{"perfil": perfil})