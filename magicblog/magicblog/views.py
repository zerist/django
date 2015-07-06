from django.http import HttpResponse
from django.template.loader import get_template 

def index(request):
    tmp = get_template("index.html")
    return HttpResponse(tmp)
