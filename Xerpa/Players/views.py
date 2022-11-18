from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .services import PlayerServices

class TodoPlayersApiView(APIView):
    def get(self, request):
        return JsonResponse(PlayerServices.get(), safe=False, status=status.HTTP_200_OK)

    def post(self, request):
        PlayerServices.create(request.data)
        return JsonResponse({'status':'User Created'}, status=status.HTTP_200_OK)

    def put(self, request):
        PlayerServices.update(request.data)
        return JsonResponse({'status':'User Update'}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        PlayerServices.delete(request.data)
        return JsonResponse({'status':'User Deleted'}, status=status.HTTP_200_OK)