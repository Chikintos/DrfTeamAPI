from django.db import models


class Team(models.Model):
    name = models.CharField("name",max_length=30,unique=True)
    def __str__(self):
        return self.name
class Player(models.Model):
    first_name = models.CharField("First name",max_length=30)
    last_name = models.CharField("Last name",max_length=30)
    email = models.EmailField("Email address", max_length=254,unique=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.team}"
    