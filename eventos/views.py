from django.shortcuts import render
from django.http import HttpResponse
import calendar 
from calendar import HTMLCalendar 
from datetime import datetime  

# Create your views here.

def home(request, year, month):
    #Change month format 
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    #Create calendar
    calendario = HTMLCalendar().formatmonth(year, month_number)
    #Get curretn year
    now = datetime.now()
    current_year = now.year

    return render(request, 'home.html', {"calendario":calendario, "current_year":current_year})