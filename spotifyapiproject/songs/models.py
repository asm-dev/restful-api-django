from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255, blank=False)
    artist = models.CharField(max_length=255, blank=True)
    album = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title()
