from django.db import models
from datetime import datetime 

# Create your models here.
class main(models.Model):
    title = models.CharField(max_length = 200, default="TEST TITLE 1")
    body = models.TextField(default="blah blah blah")
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

