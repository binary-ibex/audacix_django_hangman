from game.models import Game, Words
from game.selector import get_random_word


def create_new_game() -> Game:
    """Function to create new game"""
    random_word_obj = get_random_word()
    new_game = Game.objects.create(
        word = random_word_obj
    )
    return new_game



def update_game_state(guess: str, id: int) -> Game:
    """Function to update the game state"""
    game = Game.objects.get(id = id)

    if game.status == 3:
        return game

    if game.incorrect_guess == game.word.max_guess:
        game.status = 2
    else:
        game.player_guess += guess.lower() 
        if guess not in game.word.guess_characters:
            game.incorrect_guess += 1
        
        if game.current_word_state == game.word.word:
            game.status = 3

    game.save()
    return game


