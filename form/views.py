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

    individuals = request.POST['individuals']
    incubation = request.POST['incubation']
    symptomatic = request.POST['symptomatic']
    immunity = request.POST['immunity']
    mortality = request.POST['mortality']
    scale_city = request.POST['scale_city']
    max_rounds = request.POST['max_rounds']
    id_simulation = request.POST['id_simulation']

    parameters = {
        "individuals": individuals,
        "incubation": incubation,
        "symptomatic": symptomatic,
        "immunity": immunity,
        "mortality": mortality,
        "scale_city": scale_city,
        "max_rounds": max_rounds,
        "id_simulation": id_simulation,
    }


    return render(request, 'simulation.html',parameters)