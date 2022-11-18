from .models import Player, Team

class PlayerServices():

    def get(*request):
        try:
            return list(Player.objects.all().values())
        except Exception:
            return False

    def create(request):
        try:
            Player.objects.create(name=request['name'], goals=request['goals'], team_id=Team.objects.get(id = request['team_id']))      
            return True
        except Exception:
            return False

    def update(request):
        try:
            kwargs = {}
            if 'name' in request:
                kwargs.update({'name': request['name']})
            if 'goals' in request:
                kwargs.update({'goals': request['goals']})
            if 'team_id' in request:
                kwargs.update({'team_id': Team.objects.get(id = request['team_id'])})

            Player.objects.filter(pk=request['id']).update(**kwargs)

            return True
        except Exception:
            return False

    def delete(request):
        try:
            Player.objects.filter(pk=request['id']).delete()
            return True
        except Exception:
            return False
    