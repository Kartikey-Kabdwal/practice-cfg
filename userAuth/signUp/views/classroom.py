from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.template import RequestContext
from ..models import Room, Message,User,Student
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib import messages

class SignUpView(TemplateView):
    template_name = 'signUp/registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        else:
            return redirect('students:quiz_list')
    return render(request, 'signUp/home.html')

def handler404(request, exception, template_name="signUp/404.html"):
    response = render(None , "signUp/404.html")
    response.status_code = 404
    return response

def DiscussionView(request):
    return render(request,'signUp/discussion.html')

def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'signUp/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
    # return render(request,'signUp/room.html');

def checkview(request): 

    room = request.POST['room_name']
    # username = request.POST['username']
    user_id = request.user.id
    username=Student.objects.get(user=user_id)
    # print('-----------------------------------------------------',username)
    context={'room':room,
            'username':username,
            }
    if Room.objects.filter(name=room).exists():
        print('room already exists.....................')

        return redirect('/chat/room/'+room+'/?username='+str(username))

    else:
        # print('new room created.....................')

        # new_room = Room.objects.create(name=room)
        # new_room.save()
        # return redirect('/chat/'+room+'/?username='+username)
        messages.error(request,'Room you are looking for does not exists!')
        return HttpResponseRedirect('/discussion/',{'flag':True})
    
def send(request):
    if request.method == 'POST':
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']
        print('---------------------------------------Helloooooooooo')

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse('Message sent successfully')    

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})