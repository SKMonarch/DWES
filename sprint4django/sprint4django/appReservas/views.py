from django.shortcuts import render

from DWES.sprint4django.sprint4django.appReservas.models import Evento


# Create your views here.
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Evento
from django.views.decorators.csrf import csrf_exempt


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



