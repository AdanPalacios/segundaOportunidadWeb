from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_list_or_404, redirect
from django.core.paginator import Paginator
from .forms import formularioRegistroUsuario
from django.contrib import messages

class vistaPrincipal(View):
    def get(self, request, *args, **kwargs):

        context={

        }
        return render(request, 'pages/principal.html', context)




def login(request):
    return render(request, "pages/login.html") 



def registroUsuario(request):
    if request.method == 'POST':
        form = formularioRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
            return redirect('Home')
    else:
        form = formularioRegistroUsuario()
    context = { 'form' : form}
    return render(request, 'pages/formularioRegistro.html', context)


def ubicacion(request):
    return render(request, "pages/ubicacion.html") 

def informacionPersonal(request):
    return render(request, "pages/informacionPersonal.html") 

def editarInfoPersonal(request):
    return render(request, "pages/editarInfoPersonal.html") 

def recuperarCuenta(request):
    return render(request, "pages/recuperarCuenta.html") 