from django.shortcuts import render
from .models import Member, Group

def GetCM(request):
    return Member.objects.first()

def HomePage(request):
    member = GetCM(request)
    return render(request, 'ActionPage.html', {'member': member})

def GroupPage(request):
    member = GetCM(request)
    if member and member.group:
        group = member.group
        team = group.members.all()
        return render(request, 'ActionPage.html', {
            'member': member,
            'group': group,
            'team': team,
            'active_tab': 'group'
        })
    return render(request, 'ActionPage.html', {'member': member, 'no_group': True})

def EventsPage(request):
    member = GetCM(request)
    return render(request, 'ActionPage.html', {'member': member, 'active_tab': 'events'})

def AnnPage(request):
    member = GetCM(request)
    return render(request, 'ActionPage.html', {'member': member, 'active_tab': 'announcements'})