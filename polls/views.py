# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

def index(request):
	return HttpResponse("You are at the polls index.")

# Create your views here.
