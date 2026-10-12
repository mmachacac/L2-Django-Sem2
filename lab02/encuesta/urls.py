from django.urls import path

from . import views

app_name = "encuesta"

urlpatterns = [
    path("", views.index, name="index"),
    path("enviar/", views.enviar, name="enviar"),
    path("operaciones/", views.operaciones, name="operaciones"),
    path("operaciones/resultado/", views.resultado_operacion, name="resultado_operacion"),
    path("cilindro/", views.cilindro, name="cilindro"),
    path("cilindro/resultado/", views.resultado_cilindro, name="resultado_cilindro"),
]
