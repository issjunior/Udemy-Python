from django.http import HttpResponse

def vazio(request):
    return HttpResponse('<h1>Pagina Inigial</h1>') #dentro das aspas seria o Template