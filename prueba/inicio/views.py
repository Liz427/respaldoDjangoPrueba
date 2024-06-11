from django.shortcuts import render, HttpResponse

# Create your views here.

#Función Principal para mostrar la bienvenida.
def principal(request):
    return render(request, 'inicio/principal.html')

#Función Contacto para mostrar la información de contacto.
def contacto(request):
    return render(request, 'inicio/contacto.html')

#Función formulario para mostrar registro.
def formulario(request):
    return render(request, 'inicio/formulario.html')

def ejemplo(request):
    return render(request, 'inicio/ejemplo.html')