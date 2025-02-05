from django.shortcuts import render



# Create your views here.
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Evento, Reserva, Comentario, Usuario
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import json

@csrf_exempt
def listar_eventos(request):
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

    paginator = Paginator(eventos, limite)
    try:
        eventos_pagina = paginator.page(pagina)
    except:
        return JsonResponse({"error": "Página no válida"}, status=400)

    data = {
        "count": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": pagina,
        "next": pagina + 1 if eventos_pagina.has_next() else None,
        "previous": pagina - 1 if eventos_pagina.has_previous() else None,
        "results": [
            {
                "id": e.id,
                "titulo": e.titulo,
                "descripcion": e.descripcion,
                "fecha_hora": e.fecha_hora,
                "organizador": e.organizador.username
            }
            for e in eventos_pagina
        ]
    }

    return JsonResponse(data, safe=False)

@login_required
@csrf_exempt
def crear_evento(request):
    if request.method == "POST":
        if request.user.rol != 'organizador':
            return JsonResponse({"error": "Solo los organizadores pueden crear eventos"}, status=403)

        data = json.loads(request.body)
        evento = Evento.objects.create(
            organizador=request.user,
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            fecha_hora=data["fecha_hora"],
            capacidad=data["capacidad"],
            imagen_url=data.get("imagen_url", '')
        )
        return JsonResponse({"id": evento.id, "mensaje": "Evento creado exitosamente"})

@login_required
@csrf_exempt
def actualizar_evento(request, id):
    evento = Evento.objects.get(id=id)

    if request.user.rol != 'organizador' or evento.organizador != request.user:
        return JsonResponse({"error": "Solo los organizadores pueden actualizar eventos"}, status=403)

    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)
        evento.titulo = data.get("titulo", evento.titulo)
        evento.descripcion = data.get("descripcion", evento.descripcion)
        evento.fecha_hora = data.get("fecha_hora", evento.fecha_hora)
        evento.capacidad = data.get("capacidad", evento.capacidad)
        evento.imagen_url = data.get("imagen_url", evento.imagen_url)
        evento.save()
        return JsonResponse({"mensaje": "Evento actualizado exitosamente"})

@login_required
@csrf_exempt
def eliminar_evento(request, id):
    evento = Evento.objects.get(id=id)

    if request.user.rol != 'organizador' or evento.organizador != request.user:
        return JsonResponse({"error": "Solo los organizadores pueden eliminar eventos"}, status=403)

    evento.delete()
    return JsonResponse({"mensaje": "Evento eliminado exitosamente"})

@login_required
@csrf_exempt
def listar_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).select_related("evento")

    data = [
        {
            "id": r.id,
            "evento": r.evento.titulo,
            "entradas": r.entradas,
            "estado": r.estado
        }
        for r in reservas
    ]
    return JsonResponse(data, safe=False)

@login_required
@csrf_exempt
def crear_reserva(request):
    if request.method == "POST":
        data = json.loads(request.body)
        evento = Evento.objects.get(id=data["evento_id"])

        if evento.capacidad < data["entradas"]:
            return JsonResponse({"error": "No hay suficientes entradas disponibles"}, status=400)

        reserva = Reserva.objects.create(
            usuario=request.user,
            evento=evento,
            entradas=data["entradas"],
            estado="pendiente"
        )

        evento.capacidad -= data["entradas"]
        evento.save()

        return JsonResponse({"id": reserva.id, "mensaje": "Reserva creada exitosamente"})

@login_required
@csrf_exempt
def actualizar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)

    if request.user.rol != 'organizador':
        return JsonResponse({"error": "Solo los organizadores pueden actualizar reservas"}, status=403)

    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)
        reserva.estado = data.get("estado", reserva.estado)
        reserva.save()
        return JsonResponse({"mensaje": "Estado de la reserva actualizado"})

@login_required
@csrf_exempt
def cancelar_reserva(request, id):
    reserva = Reserva.objects.select_related("evento").get(id=id)

    if reserva.usuario != request.user:
        return JsonResponse({"error": "No puedes cancelar una reserva que no te pertenece"}, status=403)

    reserva.estado = "cancelada"
    reserva.save()

    reserva.evento.capacidad += reserva.entradas
    reserva.evento.save()

    return JsonResponse({"mensaje": "Reserva cancelada exitosamente"})

@csrf_exempt
def listar_comentarios(request, evento_id):
    comentarios = Comentario.objects.filter(evento_id=evento_id).select_related("usuario")

    data = [
        {
            "id": c.id,
            "usuario": c.usuario.username,
            "texto": c.texto,
            "fecha": c.fecha_creacion
        }
        for c in comentarios
    ]
    return JsonResponse(data, safe=False)

@login_required
@csrf_exempt
def crear_comentario(request, evento_id):
    if request.method == "POST":
        data = json.loads(request.body)
        evento = Evento.objects.get(id=evento_id)

        comentario = Comentario.objects.create(
            usuario=request.user,
            evento=evento,
            texto=data["texto"]
        )

        return JsonResponse({"id": comentario.id, "mensaje": "Comentario creado exitosamente"})



@csrf_exempt
def login_usuario(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usuario = authenticate(username=data['username'], password=data['password'])

        if usuario is not None:
            login(request, usuario)
            return JsonResponse({"mensaje": "Login exitoso"})
        else:
            return JsonResponse({"error": "Credenciales incorrectas"}, status=400)

    return JsonResponse({"mensaje": "Envía un POST con las credenciales para iniciar sesión."}, status=405)


@csrf_exempt
def registrar_usuario(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usuario = Usuario.objects.create_user(username=data["username"], password=data["password"])
        return JsonResponse({"mensaje": "Usuario registrado exitosamente"})
