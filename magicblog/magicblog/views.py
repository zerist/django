from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def index(request):
    tmp = get_template("index.html")
    return render_to_response('index.html', {})

def test(request):
    return render_to_response('test.html', {})



