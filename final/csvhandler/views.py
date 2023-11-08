from pathlib import Path
from django.shortcuts import render
from django.views import View
import csv

# Create your views here.
class Agregar(View):
    def get(self, request, nombre):
        with open('registros.csv', "a") as archivo:
            archivo.write(nombre + ',\n')
            archivo.close()

        return render(
            request,
            'csvhandler/agregar.html',
            { 'nombre': nombre }
            )
    
class Eliminar(View):
    def get(self, request, nombre):
        with open('registros.csv', "r") as archivo:
            string_crudo = archivo.read()
            archivo.close()
        string_crudo.replace(nombre +',\n','')
        with open('registros.csv', 'w') as archivo:
            archivo.write(string_crudo)
            archivo.close()
        return render(
            request,
            'csvhandler/eliminar.html',
            { 'nombre': nombre }
        )

class Listar(View):
    def get(self, request):
        print(Path(__file__).resolve().parent)
        lista = []
        with open('registros.csv', "r") as archivo:
            lectura = csv.reader(archivo)
            next(lectura)
            for fila in lectura:
                lista.append(fila[0])
            archivo.close()
            
        return render(
            request,
            'csvhandler/listar.html',
            {"registros": lista }
        )