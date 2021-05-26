from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
#from .models import Leads

simulationRunning = False

def setSimState(request):
    global simulationRunning
    if request.POST['text'] == "True":
        simulationRunning = True
    else:
        simulationRunning = False

def home(request):
    test = {
        "simRunning": simulationRunning
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