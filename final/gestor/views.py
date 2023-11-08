from django.shortcuts import render
from django.views import View
from .models import Gestor
# Create your views here.

class Agregar(View):
    def get(self, request, nombre):
        nuevo_registro = Gestor(nombre = nombre)
        nuevo_registro.save()
        return render(
            request,
            'gestor/agregar.html',
            { 'nombre': nombre }
            )
    
class Eliminar(View):
    def get(self, request, nombre):
        registros = Gestor.objects.all()
        for registro in registros:
            if registro.nombre == nombre:
                eliminar = Gestor.objects.get(id= registro.id )
                eliminar.delete()
        return render(
            request,
            'gestor/eliminar.html',
            { 'nombre': nombre }
        )

class Listar(View):
    def get(self, request):
        registros = Gestor.objects.all()
        return render(
            request,
            'gestor/listar.html',
            {"registros": registros }
        )