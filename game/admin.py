from django.contrib import admin
from .models import *
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'incorrect_guess', 'player_guess', 'status')

admin.site.register(Game, GameAdmin); 

class WordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'guess_characters', 'max_guess')

admin.site.register(Words, WordsAdmin); 