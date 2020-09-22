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
	player = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL)
	occupation = models.CharField(max_length=64, blank=True)
	age = models.IntegerField(default=20)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=SEX_MALE)
	residence = models.CharField(max_length=64, blank=True)
	birthplace = models.CharField(max_length=64, blank=True)
	strength = models.IntegerField(default=0)
	dexterity = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	constitution = models.IntegerField(default=0)
	appearance = models.IntegerField(default=0)
	power = models.IntegerField(default=0)
	size = models.IntegerField(default=0)
	education = models.IntegerField(default=0)
	move_rate = models.IntegerField(default=0)
	major_wound = models.BooleanField(default=False)
	hit_points = models.IntegerField(default=0)
	sanity = models.IntegerField(default=0)
	luck = models.IntegerField(default=0)
	magic_points = models.IntegerField(default=0)
	damage_bonus = models.IntegerField(default=0)
	build = models.IntegerField(default=0)
	personal_description = models.CharField(max_length=512, blank=True)
	ideology_and_beliefs = models.CharField(max_length=512, blank=True)
	significant_people = models.CharField(max_length=512, blank=True)
	meaningful_locations = models.CharField(max_length=512, blank=True)
	treasured_possessions = models.CharField(max_length=512, blank=True)
	traits = models.CharField(max_length=512, blank=True)
	injuries_and_scars = models.CharField(max_length=512, blank=True)
	phobias_and_manias = models.CharField(max_length=512, blank=True)
	arcane_tomes = models.CharField(max_length=512, blank=True)
	spells = models.CharField(max_length=512, blank=True)
	artifacts = models.CharField(max_length=512, blank=True)
	encounters = models.CharField(max_length=512, blank=True)
	spending_level = models.CharField(max_length=64, blank=True)
	cash = models.IntegerField(default=0)
	assets = models.CharField(max_length=512, blank=True)
	notes = models.CharField(max_length=512, blank=True)
	
	def __str__(self):
		return self.name



class Skill(models.Model):
	name = models.CharField(max_length=32)
	short_description = models.CharField(max_length=128, blank=True)
	long_description = models.CharField(max_length=512, blank=True)
	default_value = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.name