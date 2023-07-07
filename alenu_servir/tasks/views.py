from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class CustomLogoutView(LogoutView):
    next_page = 'home'

def logout(request):
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return CustomLogoutView.as_view()(request)


def signup(request):
    try:
        if request.method == 'GET':
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(request.POST['password1'])
                user.save()
                messages.success(request, '¡Registro exitoso! Inicie sesión con sus credenciales.')
                return redirect('home')
            else:
                messages.error(request, 'Ha ocurrido un error. Verifique los datos ingresados.')

    except Exception as e:
        error_message = f"Ha ocurrido un error: {str(e)}"
        messages.error(request, error_message)

    return render(request, 'signup.html', {'form': form})


def home(request):
    try:
        username = request.user.username if request.user.is_authenticated else None
        context = {'username': username}
        return render(request, 'home.html', context)
    
    except Exception as generic_error:
        error_message = f"Se produjo un error: {generic_error}"
        return render(request, 'error.html', {'error_message': error_message})
