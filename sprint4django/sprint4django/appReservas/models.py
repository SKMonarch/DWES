from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('organizador', 'Organizador'),
        ('participante', 'Participante'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='participante')
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Evento(models.Model):
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    capacidad = models.PositiveIntegerField()
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='reservas')
    entradas = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.evento.titulo}"


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.evento.titulo}"
