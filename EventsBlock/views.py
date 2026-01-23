from django.shortcuts import render, redirect
from HeartBlock.models import Group, Member
from .models import Event
from django.utils import timezone

def GetCM(request):
    return Member.objects.first()

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