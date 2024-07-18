import calendar
from calendar import HTMLCalendar

from django.shortcuts import render
from datetime import datetime


# Create your views here.

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "John"
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )
    now = datetime.now().year

    return render(request, 'home.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'name': name,
        'current_year': year
    })
