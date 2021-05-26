from django.urls import path, re_path, include

from . import views

app_name = 'form'

urlpatterns = [
    # ex: /
    path('', views.home, name='home'),
    path('simulation/', views.simulation_view, name='simulation'),
    path('set-sim-var/', views.setSimState, name='ajax-test-view'),
]