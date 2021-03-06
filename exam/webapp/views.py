from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import GuestBook
from webapp.forms import GuestBookForm

# Create your views here.


def index_view(request):
    guests = GuestBook.objects.all().filter(status='active').order_by('-date_start')
    return render(request, 'index.html', context={'guests': guests})

def add_new_guest(request, *args, **kwargs):
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'add_guest.html', context={'form': form})
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest = GuestBook.objects.create(
                user_name=form.cleaned_data['user_name'],
                user_email=form.cleaned_data['user_email'],
                user_text=form.cleaned_data['user_text']
            )
            return redirect('index')
        else:
            return render(request, 'add_guest.html', context={'form': form})


def guest_update_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = GuestBookForm(initial={
            'user_name': guest.user_name,
            'user_email': guest.user_email,
            'user_text': guest.user_text
        })
        return render(request, 'update.html', context={'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest.user_name = form.cleaned_data['user_name']
            guest.user_email = form.cleaned_data['user_email']
            guest.user_text = form.cleaned_data['user_text']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'guest': guest})