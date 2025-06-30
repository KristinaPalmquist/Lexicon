from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f'{self.name} ({self.email}) - {self.message}'
