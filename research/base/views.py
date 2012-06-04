from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from session_csrf import anonymous_csrf
from django.db.models import get_app, get_models, get_model
from models import *
from forms import *


app = get_app('base')   
model_list = get_models(app)

@anonymous_csrf
@login_required(login_url='/accounts/login/')
def home(request):
    profiles = SafeProfile.objects.all().values_list('name','price', 'manufacturer')   
    latest_safes = SafeProfile.objects.all().order_by('date_added')[0:5]
    latest_comps = SafeComponentProfile.objects.all().order_by('date_added')[0:5]
    gsform = GraphSafesForm()
    gscform = GraphSafeComponentForm()
    return render_to_response('base/home.html', {'model_list' : model_list, 'profiles' : profiles, 'latest_safes' : latest_safes, 'latest_comps' : latest_comps, 'gsform' : gsform, 'gscform' : gscform,},
        context_instance=RequestContext(request))

@anonymous_csrf
def graph_safes(request):
    profiles = SafeProfile.objects.all().values_list('name','price')   
    latest_safes = SafeProfile.objects.all().order_by('date_added')[0:5]
    latest_comps = SafeComponentProfile.objects.all().order_by('date_added')[0:5]
    if request.method == 'POST': # If the form has been submitted...
        gsform = GraphSafesForm(request.POST) # A form bound to the POST data
        if not gsform.is_valid():   
            gsform = GraphSafesForm()
    else: gsform = GraphSafesForm()
    return render_to_response('base/graphs.html', {'model_list' : model_list, 'profiles' : profiles, 'latest_safes' : latest_safes, 'latest_comps' : latest_comps, 'gsform' : gsform,},
context_instance=RequestContext(request))

@anonymous_csrf
def graph_component(request):
    profiles = SafeProfile.objects.all().values_list('name','price')   
    latest_safes = SafeProfile.objects.all().order_by('date_added')[0:5]
    latest_comps = SafeComponentProfile.objects.all().order_by('date_added')[0:5]
    if request.method == 'POST': # If the form has been submitted...
        gscform = GraphSafeComponentForm(request.POST) # A form bound to the POST data
        if not gscform.is_valid():   
            gscform = GraphSafesForm() # An unbound form
        gscform = GraphSafeComponentForm() # An unbound form
    return render_to_response('base/graphs.html', {'model_list' : model_list, 'profiles' : profiles, 'latest_safes' : latest_safes, 'latest_comps' : latest_comps, 'gscform' : gscform,},
context_instance=RequestContext(request))


@anonymous_csrf
@login_required(login_url='/accounts/login/')
def raw(request, slug):
    raw_model = get_model('base', slug)
    raw_data = raw_model.objects.all()
    return render_to_response('base/raw.html', {'model_list' : model_list, 'raw_data' : raw_data}, 
        context_instance=RequestContext(request))
