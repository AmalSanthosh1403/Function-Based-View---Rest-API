from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure database-level uniqueness
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name