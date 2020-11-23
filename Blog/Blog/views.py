from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'Hello.html', context)

def print_years(request, year):
    print(year)
    return HttpResponse(year)