from django.db import models

class ModelBox(models.Model):
    name = models.TextField()
    #height = 
    #has_color

    def __unicode__(self):
        return self.name

