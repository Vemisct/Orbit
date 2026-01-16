from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Group, Member

def WelcomePage(request):
    if request.user.is_authenticated:
        return redirect('HP')
    return render(request, 'WelcomePage.html')

def RegPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Member.objects.create(user=user, first_name=user.username, last_name="", age=18)
            login(request, user)
            return redirect('HP')
    else:
        form = UserCreationForm()
    return render(request, 'RegPage.html', {'form': form})

def AuthPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('HP')
    else:
        form = AuthenticationForm()
    return render(request, 'AuthPage.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('WlP')

def HomePage(request):
    if not request.user.is_authenticated:
        return redirect('WlP')
    
    groups = Group.objects.all()
    member = getattr(request.user, 'profile', None)
    return render(request, 'MainPage.html', {
        'groups': groups,
        'member': member
    })

def GroupPage(request):
    if not request.user.is_authenticated: return redirect('LnP')
    member = request.user.profile
    if member.group:
        return render(request, 'ActionPage.html', {
            'member': member,
            'group': member.group,
            'team': member.group.members.all(),
            'active_tab': 'group'
        })
    return redirect('HP')
def GetCM(request):
    return Member.objects.first()

def EventsPage(request):
    member = GetCM(request)
    return render(request, 'ActionPage.html', {'member': member, 'active_tab': 'events'})

def AnnPage(request):
    member = GetCM(request)
    return render(request, 'ActionPage.html', {'member': member, 'active_tab': 'announcements'})