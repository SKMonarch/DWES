"""
URL configuration for sprint4django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib import admin
from django.contrib.auth import views as auth_views
from appReservas import views

schema_view = get_schema_view(
    openapi.Info(
        title="API de Gestión de Eventos",
        default_version="v1",
        description="Documentación de la API para gestionar eventos, reservas y comentarios.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="soporte@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Panel de Administración (si lo necesitas)
    path('admin/', admin.site.urls),
    # views dinámicas Semana4
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.event_detail, name='event_detail'),
    path('reservas/crear/', views.CrearReservaAPIView.as_view(), name='crear_reserva'),
    path('user/panel/', views.user_panel, name='user_panel'),
    path('reservas/', views.ListarReservasAPIView.as_view(), name='listar_reservas'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Usuarios
    path('login/', views.LoginAPIView.as_view(), name='login_usuario'),
    path('registro/', views.RegistrarUsuarioAPIView.as_view(), name='registro_usuario'),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),

    # Eventos
    path('eventos/', views.ListarEventosAPIView.as_view(), name='listar_eventos'),
    path('eventos/crear/', views.CrearEventoAPIView.as_view(), name='crear_evento'),
    path('eventos/<int:id>/actualizar/', views.ActualizarEventoAPIView.as_view(), name='actualizar_evento'),
    path('eventos/<int:id>/eliminar/', views.EliminarEventoAPIView.as_view(), name='eliminar_evento'),

    # Reservas
    path('reservas/', views.ListarReservasAPIView.as_view(), name='listar_reservas'),
    path('reservas/<int:id>/actualizar/', views.ActualizarReservaAPIView.as_view(), name='actualizar_reserva'),
    path('reservas/<int:id>/cancelar/', views.CancelarReservaAPIView.as_view(), name='cancelar_reserva'),

    # Comentarios
    path('comentarios/<int:evento_id>/', views.ListarComentariosAPIView.as_view(), name='listar_comentarios'),
    path('comentarios/<int:evento_id>/crear/', views.CrearComentarioAPIView.as_view(), name='crear_comentario'),

    # Documentación Swagger y Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
