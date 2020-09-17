from django.shortcuts import render

from .models import Character

def index(request):
	character_list = Character.objects.all()
	context = {'character_list': character_list}
	return render(request, 'character_creator/index.html', context)
	
def sheet(request, character_id):
	context = {'character' : Character.objects.get(id=character_id) }
	return render(request, 'character_creator/sheet.html', context)
	
def creator(request):
	context = {}
	return render(request, 'character_creator/creator.html', context)
	
