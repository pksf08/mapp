from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User

@login_required
def chat_view(request, username):
    recipient = User.objects.get(username=username)
    return render(request, 'chat/chat.html', {'recipient': recipient})

@login_required
def user_list(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/user_list.html', {'users': users})
