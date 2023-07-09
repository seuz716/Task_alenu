from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.urls import reverse
from .models import Task
from .forms import TaskForm

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect(reverse('tasks:task_detail', kwargs={'pk': task.pk}))
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect(reverse('tasks:task_detail', kwargs={'pk': task.pk}))
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('tasks:task_list'))
    return render(request, 'task/task_confirm_delete.html', {'task': task})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
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

def user_logout(request):
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
