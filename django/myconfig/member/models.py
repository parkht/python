from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    hp = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username+' - '+self.name
