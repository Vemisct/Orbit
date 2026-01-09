from django.shortcuts import render


def HomePage(request):
    return render(request, 'ActionPage.html')

def EventsPage(request):
    return render(request, 'ActionPage.html', {'active_tab': 'events'})

def AnnPage(request):
    return render(request, 'ActionPage.html', {'active_tab': 'announcements'})

def GroupPage(request):
    return render(request, 'ActionPage.html', {'active_tab': 'group'})