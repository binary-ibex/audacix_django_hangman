from game.models import Game, Words


def get_random_word() -> Words:
    return Words.objects.order_by('?').first()


def get_game_by_id(id: int) -> Game:
    return Game.objects.get(id = id)