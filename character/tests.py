from django.test import TestCase

from .models import Character

class CharacterModelTests(TestCase):

	def test_derive_sanity(self):
		""" Does SAN properly derive from POW? (SAN=POW) """
		character = Character(power=30)
		character.derive_sanity()
		self.assertIs(character.sanity, 30)