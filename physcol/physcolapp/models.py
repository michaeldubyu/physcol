from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices

class Visit(models.Model):
    STATUS = Choices('CONFIRMED', 'PENDING', 'CANCELLED')
    
    visit_id = models.IntegerField(primary_key = True)
    host_id = models.IntegerField()
    speaker_id = models.IntegerField()
    status = StatusField() 
    vote = models.DecimalField(max_digits=2, decimal_places=1)
    submitted_by = models.CharField(max_length = 128) 

class Speaker(models.Model):
    speaker_id = models.IntegerField(primary_key = True)
    affiliation = models.TextField()
    research_topic = models.CharField(max_length = 512)
    name = models.CharField(max_length = 128)
    background = models.TextField()
