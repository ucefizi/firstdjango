from django.shortcuts import render
from django.http import Http404

from firstapp.models import Room


def index(request):
	rooms = Room.objects.all()
	return render(request, 'firstapp/index.html', {
		'rooms': rooms,
	})

def room_detail(request, id):
	try:
		room = Room.objects.get(id=id)
	except Room.DoesNotExist:
		raise Http404('This room does not exist')
	return render(request, 'firstapp/room_detail.html', {
		'room': room,
	})
