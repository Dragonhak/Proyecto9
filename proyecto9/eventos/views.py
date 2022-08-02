from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.

def home(request, anio, mes):
    mes = mes.title()

    #Convierte al mes de string a número:
    numero_mes = list(calendar.month_name).index(mes)
    numero_mes = int(numero_mes)

    #Crea un calendario:
    calendario = HTMLCalendar().formatmonth(
        anio, 
        numero_mes)

    return render(request, 'home.html', {
        "anio": anio,
        "mes": mes,
        "numero_mes": numero_mes,
        "calendario": calendario,
        })