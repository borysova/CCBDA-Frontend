from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def simulation_view(request):
    individuals = request.POST['individuals']
    incubation = request.POST['incubation']
    symptomatic = request.POST['symptomatic']
    immunity = request.POST['immunity']
    mortality = request.POST['mortality']
    scale_city = request.POST['scale_city']
    max_rounds = request.POST['max_rounds']
    id_simulation = request.POST['id_simulation']
    beacons_list = request.POST.getlist('beacons')

    beacons = "No"
    if len(beacons_list) != 0:
        beacons = "Yes"

    parameters = {
        "individuals": individuals,
        "incubation": incubation,
        "symptomatic": symptomatic,
        "immunity": immunity,
        "mortality": mortality,
        "scale_city": scale_city,
        "max_rounds": max_rounds,
        "id_simulation": id_simulation,
        "beacons": beacons,
    }

    return render(request, 'simulation.html', parameters)
