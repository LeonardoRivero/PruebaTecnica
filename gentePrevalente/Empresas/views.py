from django.shortcuts import render
from .serializers import EmpresaSerializer, RelacionEmpresaSerializer, ArchivosEmpresaSerializer, RelacionArchivosEmpresaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Empresa, ArchivosEmpresa
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json
from django.core.files.storage import default_storage
import os
from django.core.files import File
from django.conf import settings
# Create your views here.


class EmpresaList(APIView):
    """Lista todas las empresa o crea una nueva
    """

    def get(self, request, format=None):
        queryset = Empresa.objects.all()
        serializer = RelacionEmpresaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetail(APIView):
    """
    Recupera,Actualiza o Elimina una empresa segun su pk.
    """

    def get_object(self, pk):
        try:
            return Empresa.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = RelacionEmpresaSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = EmpresaSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchivosEmpresaList(APIView):
    """Lista todos los archivos subidos de cada empresa
    """

    def post(self, request):
        for element in request.FILES:
            archivo = request.FILES[element]
            ruta_archivo = default_storage.save(archivo.name, archivo)

        request.data["ruta_archivo"] = ruta_archivo
        serializer = ArchivosEmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        if 'idEmpresa' in request.GET:
            id_empresa = request.GET['idEmpresa']
            queryset = ArchivosEmpresa.objects.filter(empresa=id_empresa)
        else:
            queryset = ArchivosEmpresa.objects.all()
        serializer = RelacionArchivosEmpresaSerializer(queryset, many=True)
        return Response(serializer.data)


class ArchivosEmpresaDetail(APIView):
    """
    Recuepera,Actualiza o Elimina una archivo subido de una empresa segun su pk.
    """

    def get_object(self, pk):
        try:
            return ArchivosEmpresa.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            queryset = self.get_object(pk)
            location_file = queryset.ruta_archivo
            file_path = os.path.join(settings.MEDIA_ROOT, location_file)

            file_report = File(open(file_path, "rb"))
            response = HttpResponse(
                file_report, content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=%s' % location_file
            return response

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = ArchivosEmpresaSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

