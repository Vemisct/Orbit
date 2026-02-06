from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Announcement
from .form import AnnForm
from HeartBlock.models import Member
from EventsBlock.models import Event

def AnnPage(request):
    if not request.user.is_authenticated:
        return redirect('LnP')

    try:
        member = request.user.member
        if not member.group:
            messages.warning(request, "Ви не перебуваєте в групі.")
            return redirect('HP')
    except Member.DoesNotExist:
        return redirect('HP')
    announcements = Announcement.objects.filter(group=member.group)

    return render(request, 'AnnPage.html', {
        'member': member,
        'announcements': announcements,
        'active_tab': 'announcements'
    })

def CreateAnn(request):
    if not request.user.is_authenticated:
        return redirect('LnP')
        
    try:
        member = request.user.member
        group = member.group
        if not request.user.is_staff: 
            messages.error(request, "У вас немає прав для створення оголошень.")
            return redirect('AnP')
    except:
        return redirect('HP')
    
    if request.method == 'POST':
        form = AnnForm(request.POST, request.FILES)
        if form.is_valid():
            ann = form.save(commit=False)
            ann.group = group
            ann.save()
            messages.success(request, "Оголошення створено!")
            return redirect('AnP')
    else:
        form = AnnForm()
        form.fields['event'].queryset = Event.objects.filter(group=group)

    return render(request, 'AnnCreatePage.html', {'form': form})

def AnnDetailPage(request, pk):
    ann = get_object_or_404(Announcement, pk=pk)
    if not request.user.member.group or request.user.member.group != ann.group:
        messages.error(request, "Це оголошення іншої групи.")
        return redirect('HP')
        
    return render(request, 'AnnDetailPage.html', {'ann': ann})

def DeleteObject(request, obj_type, pk):
    if not request.user.is_staff:
        messages.error(request, "Недостатньо прав.")
        return redirect('HP')
    
    try:
        if obj_type == 'ann':
            obj = get_object_or_404(Announcement, pk=pk)
        elif obj_type == 'event':
            obj = get_object_or_404(Event, pk=pk)

        if obj.group == request.user.member.group:
            obj.delete()
            messages.success(request, "Об'єкт видалено.")
        else:
            messages.error(request, "Ви не можете видаляти об'єкти чужих груп.")

    except Exception as e:
        messages.error(request, "Помилка видалення.")
    
    return redirect(request.META.get('HTTP_REFERER', 'AnP'))