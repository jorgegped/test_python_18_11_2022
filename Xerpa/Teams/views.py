from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .services import TeamsServices

class TodoTeamsApiView(APIView):
    def get(self, request):
        return JsonResponse(TeamsServices.get(request), safe=False, status=status.HTTP_200_OK)

    def post(self, request):
        TeamsServices.create(request.data)
        return JsonResponse({'status':'User Created'}, status=status.HTTP_200_OK)

    def put(self, request):
        TeamsServices.update(request.data)
        return JsonResponse({'status':'User Update'}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        TeamsServices.delete(request.data)
        return JsonResponse({'status':'User Deleted'}, status=status.HTTP_200_OK)