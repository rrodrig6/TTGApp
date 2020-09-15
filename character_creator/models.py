from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=64)
	
	def __str__(self):
		return self.name

class Character(models.Model):
	SEX_MALE = 'M'
	SEX_FEMALE = 'F'
	SEX_OTHER = 'O'
	SEX_CHOICES = [
		(SEX_MALE,'Male'),
		(SEX_FEMALE, 'Female'),
		(SEX_OTHER, 'Other')
	]
	
	name = models.CharField(max_length=64)
	player = models.ForeignKey(Player, on_delete=SET_NULL)
	occupation = models.Charfield(max_length=64)
	age = models.IntegerField(default=0)
	sex = models.Charfield(max_length=1, choices=SEX_CHOICES, default=SEX_MALE)
	residence = models.CharField(max_length=64)
	birthplace = models.CharField(max_length=64)
	strength = models.IntegerField(default=0)
	dexterity = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	constitution = models.IntegerField(default=0)
	appearance = models.IntegerField(default=0)
	power = models.IntegerField(default=0)
	size = models.IntegerField(default=0)
	education = models.IntegerField(default=0)
	move_rate = models.IntegerField(default=0)
	major_wound = models.BooleanField(default=false)
	hit_points = models.IntegerField(default=0)
	sanity = models.IntegerField(default=0)
	luck = models.IntegerField(default=0)
	magic_points = models.IntegerField(default=0)
	damage_bonus = models.IntegerField(default=0)
	build = models.IntegerField(default=0)
	personal_description = models.Charfield(max_length=512)
	ideology_and_beliefs = models.Charfield(max_length=512)
	significant_people = models.Charfield(max_length=512)
	meaningful_locations = models.Charfield(max_length=512)
	treasured_possessions = models.Charfield(max_length=512)
	traits = models.Charfield(max_length=512)
	injuries_and_scars = models.Charfield(max_length=512)
	phobias_and_manias = models.Charfield(max_length=512)
	arcane_tomes = models.Charfield(max_length=512)
	spells = models.Charfield(max_length=512)
	artifacts = models.Charfield(max_length=512)
	encounters = models.Charfield(max_length=512)
	spending_level = models.Charfield(max_length=64)
	cash = models.IntegerField(default=0)
	assets = models.Charfield(max_length=512)
	notes = models.Charfield(max_length=512)
	
	def __str__(self):
		return self.name