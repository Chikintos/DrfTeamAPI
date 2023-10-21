from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,null=True)

    