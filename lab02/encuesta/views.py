from decimal import Decimal
import math

from django.shortcuts import render
from django.views.decorators.http import require_POST

def index(request):
    context = {"titulo": "Formulario de encuesta"}
    return render(request, "encuesta/formulario.html", context)


@require_POST
def enviar(request):
    context = {
        "titulo": "Respuesta de la encuesta",
        "nombre": request.POST.get("nombre", ""),
        "clave": request.POST.get("password", ""),
        "educacion": request.POST.get("educacion", ""),
        "nacionalidad": request.POST.get("nacionalidad", ""),
        "idiomas": request.POST.getlist("idiomas"),
        "correo": request.POST.get("email", ""),
        "website": request.POST.get("sitioweb", ""),
    }
    return render(request, "encuesta/respuesta.html", context)


def operaciones(request):
    return render(request, "encuesta/operaciones.html")


@require_POST
def resultado_operacion(request):
    operacion = request.POST.get("operacion", "")
    simbolos = {"suma": "+", "resta": "-", "multiplicacion": "×"}
    context = {}

    if operacion not in simbolos:
        context["error"] = "Selecciona suma, resta o multiplicación."
    else:
        try:
            valor1 = Decimal(request.POST.get("valor1", ""))
            valor2 = Decimal(request.POST.get("valor2", ""))
            if not valor1.is_finite() or not valor2.is_finite():
                raise ValueError
            if operacion == "suma":
                resultado = valor1 + valor2
            elif operacion == "resta":
                resultado = valor1 - valor2
            else:
                resultado = valor1 * valor2
            if not resultado.is_finite():
                raise ValueError
        except (ArithmeticError, ValueError):
            context["error"] = "Introduce dos números válidos dentro del rango permitido. Usa punto para los decimales."
        else:
            context.update({
                "operacion": "multiplicación" if operacion == "multiplicacion" else operacion,
                "valor1": str(valor1),
                "valor2": str(valor2),
                "simbolo": simbolos[operacion],
                "resultado": str(resultado),
            })

    return render(
        request,
        "encuesta/resultado_operacion.html",
        context,
        status=400 if "error" in context else 200,
    )


def cilindro(request):
    return render(request, "encuesta/cilindro.html")


@require_POST
def resultado_cilindro(request):
    context = {}
    try:
        altura = float(request.POST.get("altura", ""))
        diametro = float(request.POST.get("diametro", ""))
        if not all(math.isfinite(valor) and valor > 0 for valor in (altura, diametro)):
            raise ValueError
        volumen = math.pi * (diametro / 2) ** 2 * altura
        if not math.isfinite(volumen) or volumen <= 0:
            raise ValueError
    except (ValueError, OverflowError):
        context["error"] = "Introduce una altura y un diámetro mayores que cero dentro del rango permitido. Usa punto para los decimales."
    else:
        context.update({
            "altura": str(altura),
            "diametro": str(diametro),
            "volumen": format(volumen, ".10g"),
        })

    return render(
        request,
        "encuesta/resultado_cilindro.html",
        context,
        status=400 if "error" in context else 200,
    )
