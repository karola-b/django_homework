from django.shortcuts import render
from datetime import date, datetime


def is_it_monday(request):
    today = date.today()
    day_of_week = today.weekday
    is_monday = False
    if day_of_week == 0:
        is_monday = True
    return render(
        request,
        'isitmonday.html',
        context={
            "is_monday": is_monday
        }
    )
