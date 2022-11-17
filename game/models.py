from django.db import models




class Words(models.Model):
    word = models.CharField(max_length=50, null=False, blank=False)
    guess_characters = models.CharField(max_length=50, null=False, blank=False)
    max_guess = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return self.word


class Game(models.Model):
    GAME_STATE = (
        (1, "InProgress"),
        (2, "Lost"),
        (3, "Won")
    )
    word = models.ForeignKey(to=Words, on_delete=models.CASCADE)
    incorrect_guess = models.IntegerField(default=0)
    player_guess = models.CharField(max_length=50, default=" ")
    status = models.IntegerField(choices=GAME_STATE, default=1)

    @property
    def current_word_state(self):
        output = self.word.word
        for i in self.word.guess_characters:
            if i not in self.player_guess:
                output = output.replace(i, "_")
            else:
                pass
        return output

    @property
    def status_string(self):
        return [i for i in self.GAME_STATE if i[0] == self.status][0][1]
