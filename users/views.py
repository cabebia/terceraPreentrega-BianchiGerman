from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import MyUserCreationForm
def v_login(request):
    ''' V1 
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=passw)

            if user is not None:
                login(request, user)
                print("Uusario encontrado")
                return redirect('index')
            else:
                print("Uusario no encontrado")
                return render(request, 'users/login.html', {"mensaje": 'Datos incorrectos'})
        else:
            print("Formulario incorrecto")
            return render(request, 'users/login.html', {"mensaje": "Formulario incorrecto"})
    
    form = AuthenticationForm()
    '''
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        # Si se encuentra usuario lo devuelve, sino devuelve None
        if form.is_valid():
            # is_valid() es un refuerzo al sistema de autenticación.
            user = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=user, password=contra)

            login(request, user)

            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request, 'users/login.html', {"form": form})
    

    form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})

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
    form = MyUserCreationForm()

    return render(request, 'users/register.html', {'form': form})



def v_index2(request):
    return redirect('index')




