from django.db import models

# Create your models here.

class MiniBlog(models.Model):
    postName = models.CharField(max_length=100)
    publisTime = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.postName + ' | ' +  self.description[:30]
