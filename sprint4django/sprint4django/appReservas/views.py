from django.shortcuts import render

from DWES.sprint4django.sprint4django.appReservas.models import Evento


# Create your views here.
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Evento
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
def listar_eventos(request):
    titulo = request.GET.get('titulo', '')
    fecha = request.GET.get('fecha', '')
    orden = request.GET.get('orden', 'fecha_hora')
    limite = int(request.GET.get('limite', 5))
    pagina = int(request.GET.get('pagina', 1))

    eventos = Evento.objects.all()

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
        "results": [{"id": e.id, "titulo": e.titulo, "descripcion": e.descripcion, "fecha_hora": e.fecha_hora} for e in
                    eventos_pagina]
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
    if request.user.rol != 'organizador':
        return JsonResponse({"error": "Solo los organizadores pueden actualizar eventos"}, status=403)

    evento = Evento.objects.get(id=id)

    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)
        evento.titulo = data.get("titulo", evento.titulo)
        evento.descripcion = data.get("descripcion", evento.descripcion)
        evento.fecha_hora = data.get("fecha_hora", evento.fecha_hora)
        evento.capacidad = data.get("capacidad", evento.capacidad)
        evento.imagen_url = data.get("imagen_url", evento.imagen_url)
        evento.save()
        return JsonResponse({"mensaje": "Evento actualizado exitosamente"})