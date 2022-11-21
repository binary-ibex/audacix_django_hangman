from django.http import JsonResponse
from rest_framework.views import APIView, status
from game.selector import get_game_by_id 
from game.serializers import GameOutputSerializer, GameUpdateSerializer
from game.services import create_new_game, update_game_state
from django.core.exceptions import ObjectDoesNotExist



# api for creating the new game
# /game/new
class CreateGameAPI(APIView):
    def get(self, request,*args, **kwargs):
        try:
            new_game = create_new_game()
            output_data = GameOutputSerializer(new_game)
            return JsonResponse(status = status.HTTP_201_CREATED, data=output_data.data)
        except Exception as e:
            return JsonResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": f"Unknown error occured"})




# api to get the game state
# /game/<int:id>
class GetGameStateAPI(APIView):
    def get(self, request, id) -> JsonResponse:
        try:
            game = get_game_by_id(id)
            output_data = GameOutputSerializer(game)
            return JsonResponse(status = status.HTTP_200_OK, data=output_data.data)
        except ObjectDoesNotExist as e:
            return JsonResponse(status= status.HTTP_404_NOT_FOUND, data = {"error": f"Provided Id {id} doesnot exist"})
        except Exception as e:
            return JsonResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": f"Unknown error occured"})



# api to update the game state
# /game/<int:id>/guess 
class UpdateGameState(APIView):
    def put(self, request, id)-> JsonResponse:
        try:
            update_data = GameUpdateSerializer(data=request.data)
            if update_data.is_valid(raise_exception=True):
                game = update_game_state(guess = update_data.validated_data["guess"], id = id)

                output = GameOutputSerializer(game)

                return JsonResponse(status = status.HTTP_202_ACCEPTED, data=output.data)
        
        except ObjectDoesNotExist as e:
            return JsonResponse(status= status.HTTP_404_NOT_FOUND, data = {"error": f"Provided Id {id} doesnot exist"})
        except Exception as e:
            return JsonResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": f"Unknown error occured"})   
        

