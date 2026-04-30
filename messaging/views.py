from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox_view(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-sent_at')
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def sent_view(request):
    messages = Message.objects.filter(sender=request.user).order_by('-sent_at')
    return render(request, 'messaging/sent.html', {'messages': messages})

@login_required
def compose_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('messaging:inbox')
    else:
        form = MessageForm()

    return render(request, 'messaging/compose.html', {'form': form})

@login_required
def message_detail_view(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if request.user != message.receiver and request.user != message.sender:
        return redirect('messaging:inbox')

    if request.user == message.receiver and not message.is_read:
        message.is_read = True
        message.save()

    return render(request, 'messaging/detail.html', {'message': message})