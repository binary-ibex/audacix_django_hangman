from django.test import TestCase
from .models import Game, Words
from django.test import Client





class GameTestCase(TestCase):
    def setUp(self):
        Words.objects.create(word = "python",guess_characters = "py",max_guess = 2)
        Words.objects.create(word = "hangman",guess_characters = "an",max_guess = 2)
        Words.objects.create(word = "audacix",guess_characters = "dix",max_guess = 2)
        Words.objects.create(word = "bottle",guess_characters = "t",max_guess = 2)
        Words.objects.create(word = "pen",guess_characters = "en",max_guess = 2)
        

    def test_create_game(self):
        """Testing the game creation"""
        c = Client()
        response = c.get('/game/new')
        self.assertEqual(response.status_code, 201)

    def test_get_game_status(self):
        """Test for check the api to check the game status"""
        c = Client()
        _data = c.get('/game/new')
        response = c.get('/game/{}'.format(_data.json()['id']))
        self.assertEqual(response.status_code, 200)


        

        
