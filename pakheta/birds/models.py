from django.db import models

class Bird(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    background = models.TextField()
    url = models.URLField()

    
    def __str__(self):
        return self.name

class Birdset(models.Model):
    bird = models.ForeignKey(
        Bird,
        on_delete=models.CASCADE,
        related_name="birds"
    )

    image = models.ImageField(),
    audio = models.CharField(max_length=200)

    def __str__(self):
        return self.bird.name
