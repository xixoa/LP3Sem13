from email.policy import HTTP
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Sebastian Laura </h1>
    </hr>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/saludo">Saludo</a>
        </li>
        <li>
            <a href="/inicio">Monstrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15">Mostrar Números [10,15]</a>
        </li>
    </ul>
"""
def index(request):

    estudiantes = ['Luis Serna',
                'Antony Ccaccya',
                'Miguel Yauricasa',
                'Carlos Granados']
    return render(request,'index.html',{
        
        'titulo':'inicio',
        'mensaje':'Proyecto Web con Django(Desde el View)',
        'estudiantes': estudiantes

    })
def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'minombre':'Sebastian Laura'
    })
def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })
    resultado  = f"""
    <h2> Número de [{a},{b}]</h2>
    Resultado:<br>
    <ul>
    """
    while a<=b:
        resultado+= f"<li>{a}</li>"
        a+=1
    resultado+="</ul>"
    return HttpResponse(layout + resultado)
def rango2(request, a=0, b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
        <h2>Número de [{a},{b}]
    """
    resultado = f"""
        <h2>Número de [{a},{b}]</h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado+= f"<li> {a} </li>"
        a+=1
    resultado +="</ul>"
    return HttpResponse(layout + resultado)