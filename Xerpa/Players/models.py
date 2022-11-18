from django.db import models
from Teams.models import Team

    
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='')
    goals = models.IntegerField(blank=True, null=False, default=0)
    team_id = models.ForeignKey('Teams.Team', on_delete=models.PROTECT, null=False, db_column='team_id')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True, blank=False)
