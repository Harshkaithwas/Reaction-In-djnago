from django.db import models

# Create your models here.

reactions = [
    ('REAC_A', 'Reaction_A'),
    ('REAC_B', 'Reaction_B'),
    ('REAC_C', 'Reaction_C')
    ]



class postData(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField(max_length = 1000)
    reaction = models.CharField(max_length=20, choices=reactions, default=None)