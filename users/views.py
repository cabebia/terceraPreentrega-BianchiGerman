from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import EdicionPerfil, MyUserCreationForm
from .models import DatosExtra


def v_login(request):
    # V2
    if request.method == "POST":
    # CÓDIGO PARA MÉTODO <POST>

        form = AuthenticationForm(request.POST, data=request.POST)
        # Si se encuentra usuario lo devuelve, sino devuelve None
        if form.is_valid():
            # is_valid() es un refuerzo al sistema de autenticación.

            user = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            # obtenemos datos del formulario "form" limpios

            user = authenticate(username=user, password=contra)
            login(request, user)
            # usamos el módulo authenticate y login de django contrib

            DatosExtra.objects.get_or_create(user=request.user)
            # intentamos obtener los datos extras del usuario "user" y
            # si no los encuentra entonces creamos una nueva instancia del modelo "DatosExtra"
            # y se la asociamos

            # <> SI ESTAMOS ACA ES PORQUE EL USUARIO SE AUTENTICÓ Y LOGEÓ EXITOSAMENTE <> #
            return redirect('index')
        
        else:
            form = AuthenticationForm()
            return render(request, 'users/login.html', {"form": form, "mensaje": "<-> Error de inicio de sesion <->"})
    
    # CÓDIGO PARA MÉTODO <GET>

    form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form })

def v_register(request):
    ''' V1 
    if request.method == "POST":
        #form = UserRegisterForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
    '''
    if request.method == "POST":
        #form = UserRegisterForm(request.POST)
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MyUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def v_editar_perfil(request):
    datos_extra = request.user.datosextra
    # formulario = EdicionPerfil(instance=request.user, initial={'nombre_completo': datos_extra.nombre_completo, 'avatar': datos_extra.avatar, 'nivel': datos_extra.nivel, 'rango': datos_extra.rango})
    formulario = EdicionPerfil(instance=request.user, initial={'nombre_completo': datos_extra.nombre_completo})   
    
    if request.method == 'POST':

        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nuevo_nombre = formulario.cleaned_data.get('nombre_completo')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            
            if nuevo_nombre:
                datos_extra.nombre_completo = nuevo_nombre
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
                
            datos_extra.save()

            formulario.save()
            
            return redirect('editar_perfil')
    
    return render(request, 'users/editar_perfil.html', {'form': formulario})

def v_index2(request):
    return redirect('index')

class CambiarPassword(PasswordChangeView):
    template_name = 'users/cambiar_password.html'
    success_url = reverse_lazy('editar_perfil')
    ...


