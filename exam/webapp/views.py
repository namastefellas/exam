from django.shortcuts import render, redirect
from webapp.models import GuestBook

# Create your views here.


def index_view(request):
    guests = GuestBook.objects.all().filter(status='active').order_by('-date_start')
    return render(request, 'index.html', context={'guests': guests})

def add_new_guest(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'add_guest.html')
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_text = request.POST.get('user_text')

    GuestBook.objects.create(
        user_name=user_name,
        user_email=user_email,
        user_text=user_text
    )

    return redirect('index')