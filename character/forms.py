from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [ 
                    'name', 
                    'player', 
                    'occupation', 
                    'age', 
                    'sex', 
                    'residence', 
                    'birthplace', 
                    'strength', 
                    'dexterity',
                    'intelligence',
                    'constitution',
                    'appearance',
                    'power',
                    'size',
                    'education',
                    'move_rate',
                    'major_wound',
                    'hit_points',
                    'sanity',
                    'luck',
                    'magic_points',
                    'damage_bonus',
                    'build',
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
                    'encounters',
                    'spending_level',
                    'cash',
                    'assets',
                    'notes'
                    ]