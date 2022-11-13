from django.shortcuts import render
import datetime
from datetime import date, timedelta


def index(request):
    """A view to return the index page"""

    return render(request, 'home/index.html')
