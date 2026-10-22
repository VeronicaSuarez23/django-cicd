from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hola desde Django con CI/CD</h1>")