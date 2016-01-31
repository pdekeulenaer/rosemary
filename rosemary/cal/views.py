from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse

from models import Calendar

@login_required
def index(request):
    cal = Calendar.objects.filter(owner=request.user)
    html = "<ul>"

    for c in cal:
        html += "<li>%s</li>" % c

    return HttpResponse(html)
