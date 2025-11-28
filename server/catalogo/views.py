from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import CatalogoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import catalogo_model
from django.utils import timezone

from .forms import CatalogoForm

@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def productos(request):
    # se obienen todos los productos
    get_productos = catalogo_model.objects.all()
    # Se envian a serializar el objeto
    serializer = CatalogoSerializer(instance=get_productos, many=True)
    return Response({ "productos": serializer.data }, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def agregar_producto(request):
    form = CatalogoForm(request.POST, request.FILES)
    # form = request.data
    if form.is_valid():
        exist_producto = catalogo_model.objects.filter(producto=form.cleaned_data['producto'])
        # exist_trabajo = catalogo_model.objects.filter(guia=form['guia'])
        if exist_producto.exists():
            return Response({ "error": "Ya existe un producto con este nombre" })
        try:
            catalogo_model.objects.create(
                    producto = form.cleaned_data['producto'],
                    precio = form.cleaned_data['precio'],
                    dimensiones = form.cleaned_data['dimensiones'],
                    imagen = form.cleaned_data['imagen'],
                    fecha_registro = timezone.now()
                )
        except:
            return Response({ "error": "Algo salio mal" })

        return Response({ "success": "Producto cargado" }, status=status.HTTP_200_OK)
    else:
        return Response({ "error": "Formulario invalido" })

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def editar_producto(request):
    form = request.data
    exist_producto = catalogo_model.objects.filter(guia=form['guia'])
    if not exist_producto.exists():
        return Response({ "warning": "No existe el producto" }, status=status.HTTP_404_NOT_FOUND)
    # Verifica que no exista un duplicado con la misma colocación y formato
    duplicado = catalogo_model.objects.filter(producto=form['producto']).exclude(id=form['id'])  # Excluye el actual registro para permitir la actualización

    if duplicado.exists():
        return Response({ "warning": "¡Ya existe un registro con esa colocación y formato!" }, status=status.HTTP_304_NOT_MODIFIED)

    producto = catalogo_model.objects.get(guia=form['guia'])
    producto.producto = form['producto']
    producto.precio = form['precio']
    producto.dimensiones = form['dimensiones']
    producto.imagen = form['imagen']
    producto.save()

    return Response({ "success": "Producto editado" }, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def eliminar_producto(request):
    form = request.data

    exist_producto = catalogo_model.objects.filter(guia=form['guia'])
    if not exist_producto.exists():
        return Response({ "warning": "No existe el producto" }, status=status.HTTP_404_NOT_FOUND)

    producto = catalogo_model.objects.get(guia=form['guia'])
    producto.delete()

    return Response({ "success": "Producto borrado" }, status=status.HTTP_200_OK)

@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def getProductoById(request):
    data = request.data

    exist_producto = catalogo_model.objects.filter(id=data['id'])

    if not exist_producto.exists():
        return Response({ "error": "No existe el producto" }, status=status.HTTP_404_NOT_FOUND)
    producto = catalogo_model.objects.get(id=data['id'])

    serializer = CatalogoSerializer(instance=producto)
    return Response({ "producto": serializer.data }, status=status.HTTP_200_OK)