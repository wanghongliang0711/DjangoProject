from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.http import HttpResponse,JsonResponse
# Create your views here.

def homepage(request):
    template = get_template('login.html')
    # LoginResult = "1"
    html = template.render(locals())
    return HttpResponse(html)
