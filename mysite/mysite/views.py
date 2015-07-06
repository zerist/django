from django.http import HttpResponse
from django.db import connection
from django.template import Template, Context
from django.template.loader import get_template
import datetime
from django.template impport render_to_response

def hello(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title_icontains=q)
            return render_to_response('hello.html', {'books':books, 'query':q})
    return render_to_response('search_form.html', {'error':error})
