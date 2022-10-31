from .models import Message


def inbox_messages(request):
    messages = Message.objects.filter(receiver=request.user.id).filter(read=False).count()
    context = {
        'inbox_messages': messages,
    }
    return context