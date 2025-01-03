from django.db import models

# Create your models here.
# Todo(class)Table vanne class bancha django ani title vanne field bancha

class Todo(models.Model):  # PascalCase
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title   # admin side ma title dekhauxa


