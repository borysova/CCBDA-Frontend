from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render

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