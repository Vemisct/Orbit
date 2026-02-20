from django.shortcuts import render, redirect
from HeartBlock.models import Group, Member
from .models import Event
from django.utils import timezone
from .form import EventForm
from django.contrib import messages

def EventsPage(request):
    if not request.user.is_authenticated: 
        return redirect('LnP')

    try:
        member = request.user.member
    except Member.DoesNotExist:
        return redirect('HP')

    if not member.group:
        return redirect('HP')

    events = Event.objects.filter(group=member.group, date__gte=timezone.now()).order_by('date')
    
    return render(request, 'EventsPage.html', {
        'member': member,
        'group': member.group,
        'events': events,
        'active_tab': 'events'
    })

def CreateEventPage(request):
    if not request.user.is_authenticated:
        return redirect('LnP')
    if not request.user.is_superuser:
        messages.error(request, "Тільки адміністратори можуть створювати події!")
        return redirect('EvP')

    try:
        member = request.user.member
    except Member.DoesNotExist:
        return redirect('HP')

    if not member.group:
        messages.error(request, "Ви не перебуваєте в групі.")
        return redirect('HP')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.group = member.group
            event.save()
            messages.success(request, "Подію успішно заплановано!")
            return redirect('EvP')
    else:
        form = EventForm()

    return render(request, 'EventsCreatePage.html', {'form': form})