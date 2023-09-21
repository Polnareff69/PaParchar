from django.shortcuts import render
from django.http import HttpResponse
import calendar 
from calendar import HTMLCalendar 
from datetime import datetime  
from .models import Event
from .forms import VenueForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
    #Change month format 
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    #Create calendar
    calendario = HTMLCalendar().formatmonth(year, month_number)
    #Get curretn year
    now = datetime.now()
    current_year = now.year

    return render(request, 'eventos/home.html', {"calendario":calendario, "current_year":current_year})

#muestra todos los eventos
def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'eventos/eventlist.html', {'event_list':event_list})

#muestra y hace la logica de la seccion addvenue que añade un lugar
def addvenue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addvenue?submitted=True')
    else:
        form = VenueForm
        if'submitted' in request.GET:
            submitted = True

    form = VenueForm
    return render(request, 'eventos/addvenue.html', {'form':form, 'submitted':submitted})
