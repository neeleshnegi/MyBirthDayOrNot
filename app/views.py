from django.shortcuts import render
from django.http import request 

import datetime

def new(request):
    now = datetime.datetime.now()
    context = {'date' : now.day == 30 and now.month == 8 }
    return render(request,'app/new.html',context)
