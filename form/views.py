from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


#from .models import Leads


def home(request):
    test = {
        "var": True
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

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'simulation.html', {'form': form})