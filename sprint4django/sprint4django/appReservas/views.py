from django.shortcuts import render



# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Evento, Reserva, Comentario, Usuario
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'appReservas/login.html')

def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        rol = request.POST.get('rol', 'participante')
        if not username or not password:
            messages.error(request, 'Todos los campos son obligatorios.')
        else:
            try:
                usuario = Usuario.objects.create_user(username=username, password=password, rol=rol)
                login(request, usuario)
                return redirect('index')
            except Exception as e:
                messages.error(request, f'Error al registrar el usuario: {str(e)}')
    return render(request, 'appReservas/registro.html')

def index(request):
    eventos = Evento.objects.all()
    return render(request, 'appReservas/index.html', {'eventos': eventos})

def event_detail(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'appReservas/event_detail.html', {'evento': evento})

@login_required
def user_panel(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'appReservas/user_panel.html', {'reservas': reservas})

# Permisos personalizados
class EsOrganizador(BasePermission):
    def has_permission(self, request, view):
        return request.user.rol == 'organizador'

class EsParticipante(BasePermission):
    def has_permission(self, request, view):
        return request.user.rol == 'participante'

# Autenticación y Registro de Usuarios
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario:
            token, _ = Token.objects.get_or_create(user=usuario)
            return Response({"token": token.key}, status=HTTP_200_OK)
        return Response({"error": "Credenciales incorrectas"}, status=HTTP_400_BAD_REQUEST)

class RegistrarUsuarioAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        rol = request.data.get('rol', 'participante')
        if not username or not password or rol not in ['organizador', 'participante']:
            return Response({"error": "Datos inválidos"}, status=HTTP_400_BAD_REQUEST)
        usuario = Usuario.objects.create_user(username=username, password=password, rol=rol)
        Token.objects.create(user=usuario)
        return Response({"mensaje": "Usuario registrado exitosamente"}, status=HTTP_201_CREATED)

# Vistas para Eventos


class ListarEventosAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Listar eventos.",
        manual_parameters=[
            openapi.Parameter('titulo', openapi.IN_QUERY, description="Filtrar por título del evento",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('fecha', openapi.IN_QUERY, description="Filtrar por fecha del evento (YYYY-MM-DD)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('orden', openapi.IN_QUERY, description="Ordenar por un campo (por defecto: fecha_hora)",
                              type=openapi.TYPE_STRING, default='fecha_hora'),
            openapi.Parameter('limite', openapi.IN_QUERY, description="Cantidad de eventos por página (por defecto: 5)",
                              type=openapi.TYPE_INTEGER, default=5),
            openapi.Parameter('pagina', openapi.IN_QUERY, description="Número de página (por defecto: 1)",
                              type=openapi.TYPE_INTEGER, default=1),
        ]
    )

    def get(self, request):
        titulo = request.GET.get('titulo', '')
        fecha = request.GET.get('fecha', '')
        orden = request.GET.get('orden', 'fecha_hora')
        limite = int(request.GET.get('limite', 5))
        pagina = int(request.GET.get('pagina', 1))

        eventos = Evento.objects.select_related("organizador").all()
        if titulo:
            eventos = eventos.filter(titulo__icontains=titulo)
        if fecha:
            eventos = eventos.filter(fecha_hora__date=fecha)
        eventos = eventos.order_by(orden)

        paginador = Paginator(eventos, limite)
        try:
            eventos_pagina = paginador.page(pagina)
        except:
            return Response({"error": "Página no válida"}, status=HTTP_400_BAD_REQUEST)

        datos = {
            "total": paginador.count,
            "paginas": paginador.num_pages,
            "pagina_actual": pagina,
            "siguiente": pagina + 1 if eventos_pagina.has_next() else None,
            "anterior": pagina - 1 if eventos_pagina.has_previous() else None,
            "resultados": [
                {
                    "id": evento.id,
                    "titulo": evento.titulo,
                    "descripcion": evento.descripcion,
                    "fecha_hora": evento.fecha_hora,
                    "organizador": evento.organizador.username
                }
                for evento in eventos_pagina
            ]
        }
        return Response(datos)

class CrearEventoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, EsOrganizador]

    def post(self, request):
        datos = request.data
        evento = Evento.objects.create(
            organizador=request.user,
            titulo=datos.get("titulo"),
            descripcion=datos.get("descripcion"),
            fecha_hora=datos.get("fecha_hora"),
            capacidad=datos.get("capacidad"),
            imagen_url=datos.get("imagen_url", '')
        )
        return Response({"id": evento.id, "mensaje": "Evento creado exitosamente"}, status=HTTP_201_CREATED)

class ActualizarEventoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, EsOrganizador]

    def put(self, request, id):
        evento = get_object_or_404(Evento, id=id)
        if evento.organizador != request.user:
            return Response({"error": "No tienes permiso para actualizar este evento"}, status=HTTP_403_FORBIDDEN)
        datos = request.data
        evento.titulo = datos.get("titulo", evento.titulo)
        evento.descripcion = datos.get("descripcion", evento.descripcion)
        evento.fecha_hora = datos.get("fecha_hora", evento.fecha_hora)
        evento.capacidad = datos.get("capacidad", evento.capacidad)
        evento.imagen_url = datos.get("imagen_url", evento.imagen_url)
        evento.save()
        return Response({"mensaje": "Evento actualizado exitosamente"})

    def patch(self, request, id):
        return self.put(request, id)

class EliminarEventoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, EsOrganizador]

    def delete(self, request, id):
        evento = get_object_or_404(Evento, id=id)
        if evento.organizador != request.user:
            return Response({"error": "No tienes permiso para eliminar este evento"}, status=HTTP_403_FORBIDDEN)
        evento.delete()
        return Response({"mensaje": "Evento eliminado exitosamente"})

# Vistas para Reservas

class ListarReservasAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservas = Reserva.objects.filter(usuario=request.user).select_related("evento")
        datos = [
            {
                "id": reserva.id,
                "evento": reserva.evento.titulo,
                "entradas": reserva.entradas,
                "estado": reserva.estado
            }
            for reserva in reservas
        ]
        return Response(datos)

class CrearReservaAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        datos = request.data
        evento = get_object_or_404(Evento, id=datos.get("evento_id"))
        if evento.capacidad < datos.get("entradas", 0):
            return Response({"error": "No hay suficientes entradas disponibles"}, status=HTTP_400_BAD_REQUEST)
        reserva = Reserva.objects.create(
            usuario=request.user,
            evento=evento,
            entradas=datos.get("entradas"),
            estado="pendiente"
        )
        evento.capacidad -= datos.get("entradas")
        evento.save()
        return Response({"id": reserva.id, "mensaje": "Reserva creada exitosamente"}, status=HTTP_201_CREATED)

class ActualizarReservaAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, EsOrganizador]

    def put(self, request, id):
        reserva = get_object_or_404(Reserva, id=id)
        datos = request.data
        reserva.estado = datos.get("estado", reserva.estado)
        reserva.save()
        return Response({"mensaje": "Estado de la reserva actualizado"})

    def patch(self, request, id):
        return self.put(request, id)

class CancelarReservaAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        reserva = get_object_or_404(Reserva.objects.select_related("evento"), id=id)
        if reserva.usuario != request.user:
            return Response({"error": "No puedes cancelar una reserva que no te pertenece"}, status=HTTP_403_FORBIDDEN)
        reserva.estado = "cancelada"
        reserva.save()
        reserva.evento.capacidad += reserva.entradas
        reserva.evento.save()
        return Response({"mensaje": "Reserva cancelada exitosamente"})

# Vistas para Comentarios

class ListarComentariosAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, evento_id):
        comentarios = Comentario.objects.filter(evento_id=evento_id).select_related("usuario")
        datos = [
            {
                "id": comentario.id,
                "usuario": comentario.usuario.username,
                "texto": comentario.texto,
                "fecha": comentario.fecha_creacion
            }
            for comentario in comentarios
        ]
        return Response(datos)

class CrearComentarioAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, evento_id):
        datos = request.data
        evento = get_object_or_404(Evento, id=evento_id)
        comentario = Comentario.objects.create(
            usuario=request.user,
            evento=evento,
            texto=datos.get("texto")
        )
        return Response({"id": comentario.id, "mensaje": "Comentario creado exitosamente"}, status=HTTP_201_CREATED)