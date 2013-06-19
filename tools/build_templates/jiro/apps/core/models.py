from django.db import models

class ModelBox(models.Model):
    name = models.CharField(max_length=30)
    height = models.IntegerField() 
    has_color = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.name

