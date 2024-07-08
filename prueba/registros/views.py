from django.shortcuts import render, get_object_or_404
from .models import Alumnos, ComentarioContacto
#Accedemos al modelo Alumnos que contiene la estructura de la tabla
from .forms import ComentarioContactoForm

# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all()
    #all recupera todos los objetos  del modelo (registros de la tabla alumnos)
    return render(request, "registros/principal.html",{'9B':alumnos})
#indicamos el lugar donde se renderizará el resultado de esta vista
#y enviamos la lista de alumnos recuperados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #si los datos recibidos son correctos
            form.save() #inserta
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/consultarComentario.html',{'comentarios':comentarios})
    form = ComentarioContactoForm()
    #si algo sale mal, se reenvían al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form':form})

def contacto(request):
    return render(request, 'registros/contacto.html')
    #Indicamos el ligar donde se renderizará el resultado de esta vista

def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/consultarComentario.html', {'comentarios':comentarios})

def eliminarComentarioContacto(request, id, confirmacion = 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id = id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/consultarComentario.html', {'comentarios':comentarios})
    
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"registros/editarComentario.html", {'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id = id)
    form = ComentarioContactoForm(request.POST, instance = comentario)
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/consultarComentario.html', {'comentarios':comentarios})
    return render(request, 'registros/editarComentario.html', {'comentario', comentario})