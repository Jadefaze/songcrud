from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.last_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title
    

class Lyric(models.Model):
    content = models.CharField(max_length=3000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_id

