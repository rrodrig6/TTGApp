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
		if int(request.POST['d_val']) == 100:
			d_result = randint(1,100)
			if 'character_id' in request.POST and 'roll_skill' in request.POST:
				character = Character.objects.get(id=request.POST['character_id'])
				message_out = character.roll_against_skill(request.POST['roll_skill'], d_result)
			else:
				if(d_result<2):
					message_out = 'Critical Success!'
				elif(d_result<11):
					message_out = 'Extreme Success!'
				elif(d_result<26):
					message_out = 'Hard Success!'
				elif(d_result<51):
					message_out = 'Regular Success!'
				elif(d_result<96):
					message_out = 'FAILURE'
				else:
					message_out = 'FUMBLE'
			return JsonResponse({'d_result':str(d_result), 'message_out':message_out}, status=200)
		else:
			return JsonResponse({'error':'d_val_error'})
