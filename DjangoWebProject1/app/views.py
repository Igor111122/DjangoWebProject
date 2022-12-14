"""
Definition of views.
"""

from datetime import datetime
from random import random
from django.shortcuts import render
from django.http import HttpRequest
import random

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'temp':tamp,
            'water':weter,
        }
    )
    
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def temp():
    return random.randint (14,24)

def water():
    return random.randint (10,60)

tamp = random.randint (14,24)
weter = random.randint (10,60)