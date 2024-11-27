from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tjuegos
from .models import Tcomentarios
import json
import django.views.decorators.csrf import csrf_exempt

def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola caracola</h1>");

def devolver_juegos(request):
	juego = Tjuegos.objects.all()
	respuesta = [
		{
			'id': juego.id,
			'nombre': juego.nombre,
			'url_imagen': juego.url_imagen,
			'fecha_lanzamiento': juego.fecha_lanzamiento,
			'genero':juego.genero
		}
		for juego in juego
	]
	return JsonResponse(respuesta,safe=False,json_dumps_params={'ensure_ascii':False})	

def devolver_juego_por_id(request, id_juego):
    try:
        juego = Tjuegos.objects.get(pk=id_juego)
        respuesta = {
            'id': juego.id,
            'nombre': juego.nombre,
            'url_imagen': juego.url_imagen,
            'fecha_lanzamiento': juego.fecha_lanzamiento,
            'genero': juego.genero,
            'comentarios': [
                {
                    'id': comentario.id,
                    'comentario': comentario.comentario,
                    'usuario': comentario.usuario.nombre if comentario.usuario else None,
                    'fecha': comentario.fecha
                }
                for comentario in juego.tcomentarios_set.all()
            ]
        }
        return JsonResponse(respuesta, json_dumps_params={'ensure_ascii': False})
    except Tjuegos.DoesNotExist:
        return JsonResponse({'error': 'Juego no encontrado'}, status=404)
    


	

@csrf_exempt

def crear_comentario(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        try:
            nuevo_comentario = Tcomentarios(
                comentario=datos['comentario'],
                usuario_id=datos.get('usuario_id'),
                juego_id=datos['juego_id'],
                fecha=datos['fecha']
            )
            nuevo_comentario.save()
            return JsonResponse({}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)