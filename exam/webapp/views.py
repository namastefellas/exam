from django.shortcuts import render
from webapp.models import GuestBook

# Create your views here.


def index_view(request):
    guests = GuestBook.objects.all().filter(status='active').order_by('-date_start')
    return render(request, 'index.html', context={'guests': guests})