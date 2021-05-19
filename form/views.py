from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


#from .models import Leads
#test


def home(request):
    test = {
        "var": False
    }
    return render(request, 'index.html', test)

def simulation_view(request):
    return render(request, 'simulation.html')

"""
def signup(request):
    leads = Leads()
    status = leads.insert_lead(request.POST['name'], request.POST['email'], request.POST['previewAccess'])
    return HttpResponse('', status=status)
"""