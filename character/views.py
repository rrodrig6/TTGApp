from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.shortcuts import render

from django.urls import reverse
from django.views import generic

from .models import Character
from .forms import CharacterForm

from random import randint

class IndexView(generic.ListView):
	template_name = 'character/index.html'
	#context_object_name = 'character_list'
	
	def get_queryset(self):
		return Character.objects.all()

class DetailView(generic.DetailView):
	model = Character
	template_name = 'character/sheet.html'

def play(request, pk):
	character = Character.objects.get(id=pk)
	return render(request, 'character/play.html', {'character':character})

def create(request):

	if request.method == 'POST':

		form = CharacterForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('character:sheet', args=[form.instance.id]))

	else:
			form = CharacterForm()

	return render(request,'character/create.html', {'form':form})
	

def roll(request, pk):
	if request.is_ajax and request.method == 'POST':
		if int(request.POST['dVal']) == 100:
			dResult = randint(1,100)
			return JsonResponse({'dResult':str(dResult)}, status=200)
		else:
			return JsonResponse({'error':'dValError'})