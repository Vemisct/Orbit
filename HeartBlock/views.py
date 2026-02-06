from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Group, Member
from .form import *
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

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
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': 'form-control bg-main', 'placeholder': 'Введіть дані'})
            
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
    try:
        member = request.user.member
    except Member.DoesNotExist:
        member = Member.objects.create(user=request.user, first_name=request.user.username)

    groups = Group.objects.all()
    return render(request, 'MainPage.html', {
        'groups': groups,
        'member': member
    })

def GroupPage(request, group_id):
    if not request.user.is_authenticated: return redirect('LnP')
    
    group = get_object_or_404(Group, id=group_id)
    member, _ = Member.objects.get_or_create(user=request.user)
    
    if member.group == group:
        return redirect('GrMP')

    return render(request, 'GroupPage.html', {
        'group': group,
        'member': member,
    })

def JoinGroup(request, group_id):
    if not request.user.is_authenticated: return redirect('LnP')
    
    group = get_object_or_404(Group, id=group_id)
    member, _ = Member.objects.get_or_create(user=request.user)
    
    if not group.is_full:
        member.group = group
        member.save()
    
    return redirect('GrMP')

def LeaveGroup(request):
    if not request.user.is_authenticated: return redirect('LnP')
    
    member = request.user.member
    member.group = None
    member.save()
    
    return redirect('HP')

def MemberGroupPage(request):
    if not request.user.is_authenticated: return redirect('LnP')
    
    member = request.user.member
    if not member.group:
        return redirect('HP')
        
    return render(request, 'MemberGroupPage.html', {
        'group': member.group,
        'team': member.group.members.all(),
        'active_tab': 'group'
    })
def GetCM(request):
    return Member.objects.first()

def AnnPage(request):
    if not request.user.is_authenticated: return redirect('LnP')

    if not hasattr(request.user, 'member') or not request.user.member.group:
        return redirect('HP')

    member = GetCM(request)
    return render(request, 'ActionPage.html', {'member': member, 'active_tab': 'announcements'})

def ProfilePage(request):
    if not request.user.is_authenticated: return redirect('LnP')
    member = request.user.member
    return render(request, 'ProfilePage.html', {'member': member})
def SettingsPage(request):
    if not request.user.is_authenticated: return redirect('LnP')
    return render(request, 'SettingsPage.html')

def AboutGroupPage(request, group_id):
    if not request.user.is_authenticated: return redirect('LnP')
    
    group = get_object_or_404(Group, id=group_id)
    member = request.user.member
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.group = group
            comment.author = member
            comment.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'content': comment.content,
                    'author': f"{comment.author.first_name} {comment.author.last_name}",
                    'username': comment.author.user.username,
                    'created_at': "Щойно",
                    'id': comment.id,
                    'delete_url': reverse('DlCm', kwargs={'pk': comment.pk})
                })
            
            messages.success(request, "Коментар опубліковано!")
            return redirect('AbGrP', group_id=group.id)
    else:
        form = CommentForm()

    comments = group.comments.all()

    return render(request, 'AboutGroupPage.html', {
        'group': group,
        'member': member,
        'comments': comments,
        'form': form,
        'active_tab': 'about'
    })

def DeleteComment(request, pk):
    comment = get_object_or_404(GroupComment, pk=pk)
    if comment.author == request.user.member and comment.can_be_deleted:
        comment.delete()
        messages.success(request, "Коментар видалено.")
    else:
        messages.error(request, "Час на видалення вийшов або ви не автор.")

    return redirect(request.META.get('HTTP_REFERER', 'AbGrP'))

def ProfileEditPage(request):
    if not request.user.is_authenticated: return redirect('LnP')
    member = request.user.member
    
    if request.method == 'POST':
        form = MemberEditForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, "Профіль оновлено!")
            return redirect('PrP')
        else:
            messages.error(request, "Помилка при збереженні.")
    else:
        form = MemberEditForm(instance=member)
    
    return render(request, 'ProfileRedPage.html', {'form': form, 'member': member})

def ShopPage(request):
    return render(request, 'ShopPage.html')

@csrf_exempt
def PaymentSuccess(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            member = request.user.member
            member.is_premium = True
            member.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)