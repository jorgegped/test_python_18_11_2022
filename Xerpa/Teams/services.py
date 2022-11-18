from django.db.models import Sum

from .models import Team
from Players.models import Player


class TeamsServices():

    def get(request):
        try:
            if request.GET.getlist('team'):
                teams = list(Team.objects.filter(id=request.GET.getlist('team')[0]).values())

            else:   
                teams = list(Team.objects.all().values())
                
            for team in teams:
                goals = Player.objects.filter(team_id=team['id']).aggregate(Sum('goals'))
                team['goals_count']=goals['goals__sum']

            return teams
            
        except Exception as exec:
            print(exec)
            return False

    def create(request):
        try:
            Team.objects.create(name=request['name'], city=request['city'])      
            return True
        except Exception:
            return False

    def update(request):
        try:
            kwargs = {}
            if 'name' in request:
                kwargs.update({'name': request['name']})
            if 'goals' in request:
                kwargs.update({'city': request['city']})

            Team.objects.filter(pk=request['id']).update(**kwargs)

            return True
        except Exception:
            return False

    def delete(request):
        try:
            Team.objects.filter(pk=request['id']).delete()
            return True
        except Exception:
            return False
    