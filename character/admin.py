from django.contrib import admin

from .models import Player, Character, Skill

class CharacterAdmin(admin.ModelAdmin):
	fieldsets = [
		('Investigator',
			{'fields': [
				'name',
				'player',
				'occupation'
				]}),
		('Background', 
			{'classes': ('collapse',),
			 'fields': [
				('age', 'sex'),
				('residence', 'birthplace')
				]}),
		('Characteristics',
			{'classes': ('collapse',),
			 'fields': [
				('strength', 'dexterity', 'intelligence'),
				('constitution', 'appearance', 'power'),
				('size', 'education', 'move_rate')
				]}),
		('Status',
			{'classes': ('collapse',),
			 'fields': [
				'major_wound',
				('hit_points', 'sanity'),
				('luck', 'magic_points')
				]}),
		('Combat',
			{'classes': ('collapse',),
			 'fields': [
				'damage_bonus',
				'build'
				]}),
		('Backstory',
			{'classes': ('collapse','wide'),
			 'fields': [
				'personal_description',
				'ideology_and_beliefs',
				'significant_people',
				'meaningful_locations',
				'treasured_possessions',
				'traits',
				'injuries_and_scars',
				'phobias_and_manias',
				'arcane_tomes',
				'spells',
				'artifacts',
				'encounters'
				]}),
		('Cash & Assets',
			{'classes': ('collapse',),
			 'fields': [
				'spending_level',
				'cash',
				'assets'
				]}),
		('None',
			{'classes': ('collapse','wide'),
			 'fields': [
				'notes'
				]})
		]
		
	list_display = ('name', 'occupation', 'age', 'sex', 'personal_description', 'player')

admin.site.register(Player)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Skill)