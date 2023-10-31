from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def v_login(request):
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
    return render(request, 'users/login.html', {"form": form})

def v_register(request):
    if request.method == "POST":
        #form = UserRegisterForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})






