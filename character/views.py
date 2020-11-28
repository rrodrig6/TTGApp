from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.shortcuts import render

from django.urls import reverse
from django.views import generic

from .models import Character
from .forms import CharacterForm

from random import randint
from math import floor

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
		debug_out = ''
		if int(request.POST['d_val']) == 100:
			d_result = randint(1,100)
			# Process bonus/penalty dice rolls
			if 'num_bonus_dice' in request.POST:
				bonus_dice = int(request.POST['num_bonus_dice'])
				d_result_ones = d_result % 10
				d_result_tens = floor(d_result/10)
				debug_out += "Original Ones: " + str(d_result_ones) + "<br>"
				debug_out += "Original Tens: " + str(d_result_tens) + "<br>"
				if bonus_dice < 0:
					while(bonus_dice != 0):
						bonus_die_value = randint(1,10)
						debug_out += "Penalty Tens: " + str(bonus_die_value) + "<br>"
						if(bonus_die_value > d_result_tens):
							d_result_tens = bonus_die_value
						bonus_dice += 1
				if bonus_dice > 0:
					while(bonus_dice !=0):
						bonus_die_value = randint(1,10)
						debug_out += "Bonus Tens: " + str(bonus_die_value) + "<br>"
						if(bonus_die_value < d_result_tens):
							d_result_tens = bonus_die_value
						bonus_dice -= 1
				d_result = (d_result_tens * 10) + d_result_ones
				if d_result > 100:
					d_result = 100
			# Process Character skill roll
			if 'character_id' in request.POST and 'roll_skill' in request.POST and request.POST['roll_skill'] != "":
				character = Character.objects.get(id=request.POST['character_id'])
				message_out = character.roll_against_skill(request.POST['roll_skill'], d_result)
			# Contextless dice roll
			else:
				message_out = "--"
			return JsonResponse({'d_result':str(d_result), 'message_out':message_out, 'debug_out': debug_out}, status=200)
		else:
			return JsonResponse({'error':'d_val_error', 'debug_out': debug_out})
