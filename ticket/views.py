from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Ticket
# Create your views here.


@login_required
def index(request):
    active_tickets = Ticket.get_all_active_tickets()
    context = {'active_tickets': active_tickets}

    return render(request, 'ticket/index.html', context)


@login_required
def all(request):
    return HttpResponse("All Portion")


@login_required
def detail(request):
    return HttpResponse("Detail Portion")
