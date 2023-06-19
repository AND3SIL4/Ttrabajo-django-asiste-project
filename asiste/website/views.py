from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Aprendiz

# Create your views here.
def landing(request):
    return render(request, 'landing_page.html', {})

def home(request):
  aprendices = Aprendiz.objects.all()
  # Check to see if loggin in
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      # Authenticate
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          messages.success(request, "Bienvenido a asisite...")
          return redirect('home')
      else:
          messages.success(request, "Usuario no valido para ingresar")
          return redirect('home')
  else:
      return render(request, 'home.html', {'aprendices': aprendices})

def logout_user(request):
    logout(request)
    messages.success(request, "Haz cerrado tu sesion...")
    return redirect('home')

def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      # Authenticate and login
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, "Primera vez en asiste... cool!")
      return redirect('home')
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form':form})
  return render(request, 'register.html', {'form':form})

def aprendiz_view(request, pk):
  if request.user.is_authenticated:
    # look up records
    view = Aprendiz.objects.get(documento_aprendiz=pk)
    return render(request, 'aprendiz.html', {'aprendiz_view': view})
  else:
    messages.success(request, "No puedes acceder a la informacion")
    return redirect('home')

def delete_record(request, pk):
  if request.user.is_authenticated:
    delete_it = Aprendiz.objects.get(documento_aprendiz=pk)
    delete_it.delete()
    messages.success(request, "Registro eliminado correctamente...")
    return redirect('home')
  else:
    messages.success(request, "No haz iniciado sesión...")
    return redirect('home')

def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro creado con exito...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "No puedes hacer registros...")
		return redirect('home')

def update_record(request, pk):
  if request.user.is_authenticated:
      current_record = Aprendiz.objects.get(documento_aprendiz=pk)
      form = AddRecordForm(request.POST or None, instance=current_record)
      if form.is_valid():
          form.save()
          messages.success(request, "Yup....")
          return redirect('home')
      return render(request, 'update_record.html', {'form':form})
  else:
    messages.success(request, "You Must Be Logged In...")
    return redirect('home')
