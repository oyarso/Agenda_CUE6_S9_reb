from django.http import HttpResponseRedirect 

from tokenize import PseudoExtras 
from django.views.generic import TemplateView 
from django.shortcuts import render  
from .forms import WidgetForm, BoardsForm, RegistroUsuarioForm 
from django.contrib import messages 
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm 




def widgetform_view(request): 
    return render(request, "widgetform.html") 

class Libro(object): 
    def __init__ (self, titulo, autor, valoracion): 
        self.titulo=titulo 
        self.autor=autor   
        self.valoracion=  valoracion 

class IndexPageView(TemplateView): 
    template_name = "index.html" 
    
def menuView(request): 
    template_name = 'menu.html' 
    return render(request, template_name) 

def mostrar(request): 
    libro1 = Libro("Django 3 Web Development Cookbook Fourth Edition", "Aidas Bendoraitis", 3250)
    libro2 = Libro("Two Scoops of Django 3.x", "Daniel Feldroy", 1570)
    
    libro3 = Libro("Django for Professionals", "William S. Vincent", 2100)
    libro4 = Libro("Django for APIs", " William S. Vincent", 2540)

    libro5 = Libro("El libro de Django", "Adian Holovaty",0)
    libro6 = Libro("Python Web Development with Django", "Jeff Forcier",9) 

    items=[libro1,libro2,libro5,libro6,libro3,libro4]  



    context = {"items" : items} 
    return render(request, "templatesexample.html", context) 


def datosform_view(request): 
    context ={} 
    return render(request, "datosform.html", context) 

def boardsform_view(request): 
    context ={}  
    form = BoardsForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect('/')  
    context['form']= form 
    return render(request, "datosform.html", context) 

def widget_view(request): 
    context = {} 
    form = WidgetForm(request.POST or None) 
    context['form'] = form 
    return render(request, "widget_home.html", context) 

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/menu')
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos.")
    else:
        form = RegistroUsuarioForm()
        
    return render(request=request, template_name="registration/registro.html", context={"register_form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/menu')
            else:
                messages.error(request, "Invalido username o password.")
        else:
            messages.error(request, "Invalido username o password.")
    else:
        form = AuthenticationForm()
    
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/menu')