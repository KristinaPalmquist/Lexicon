from django.db import models

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserProfile(models.Model):
    webpage = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} | {self.webpage}"
