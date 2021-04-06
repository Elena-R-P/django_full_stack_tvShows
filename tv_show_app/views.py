from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    return redirect('/shows')

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)

def create_new(request):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        show = Show.objects.create(
            show_title = request.POST['title'], 
            show_network = request.POST['network'], 
            show_desc = request.POST['desc'], 
            show_release_date = request.POST['release_date']
        )
    return redirect(f'/shows/details_page/{show.id}') 

def shows_new(request):
    return render(request, 'show_create.html')


def details_page(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'details_page.html', context)

def edit_page(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'show_edit.html', context)

def update(request, show_id):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/edit_page/{show_id}')
    else:
        show = Show.objects.get(id=show_id)
        show.show_title = request.POST['title']
        show.show_network = request.POST['network'] 
        show.show_desc = request.POST['desc'] 
        show.show_release_date = request.POST['release_date']
        show.save()
        return redirect(f'/shows/details_page/{show_id}')

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
