from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse

from .models import Character

def index(request):
	character_list = Character.objects.all()
	context = {'character_list': character_list}
	return render(request, 'character/index.html', context)
	
def sheet(request, character_id):
	context = {'character' : Character.objects.get(id=character_id) }
	return render(request, 'character/sheet.html', context)
	
def create(request):
	if request.method == 'POST':
		character = Character(
			name = request.POST['name'],
			occupation = request.POST['occupation'],
			age = request.POST['age'],
			sex = request.POST['sex'],
			strength = request.POST['strength'],
			dexterity = request.POST['dexterity'],
			intelligence = request.POST['intelligence'],
			constitution = request.POST['constitution'],
			appearance = request.POST['appearance'],
			power = request.POST['power'],
			size = request.POST['size'],
			education = request.POST['education'],
			luck = request.POST['luck'],
			)
		character.save()
		return HttpResponseRedirect(reverse('character:sheet', args=[character.id]))
	else:
		context = {}
		return render(request, 'character/create.html', context)
	
