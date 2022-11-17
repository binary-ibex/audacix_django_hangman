from rest_framework import serializers

from game.models import Game, Words

class WordOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ["id"]
        
class GameOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "incorrect_guess", "current_word_state", "status_string"]


class GameUpdateSerializer(serializers.Serializer):
    guess = serializers.CharField(max_length=1)
    