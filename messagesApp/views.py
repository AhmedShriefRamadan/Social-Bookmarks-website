from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Message
from actions.utils import create_action


@login_required
def message_create(request, uid):
    user = get_object_or_404(User, id=uid)
    if request.method == 'POST':
        message = request.POST['message']
        if message:
            Message.objects.create(message_from=request.user,
                                    message_to=user,
                                    content=message)
            # create_action(request.user, 'Send you a message')
    messages_from = list(Message.objects.filter(message_from=request.user,
                                            message_to=user))
    messages_to = list(Message.objects.filter(message_from=user,
                                            message_to=request.user))

    messages_all = messages_from + messages_to
    messages_all.sort(key=lambda x: x.created)
    
    return render(request,
                    'messagesApp/create.html',
                    {'messages_all':messages_all,
                    'user':user,
                    'section':'messages',
                    'messages_from':messages_from})

@login_required
def message_list_users(request):
    users = User.objects.exclude(username=request.user)
    following_id = request.user.following.values_list('id',flat=True)
    users = users.filter(id__in=following_id)
    return render(request,
                    'messagesApp/message_users.html',
                    {'users':users,
                    'section':'message'})
