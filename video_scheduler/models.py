from django.db import models

# Create your models here.

class Video(models.Model):
    video_title = models.TextField(max_length=100, primary_key=True)
    video_length = models.TextField(max_length=100)
    video_description = models.TextField(max_length=100)

    def __repr__(self):
        return "Video Title {} : Description {} : Length{}".format(
            self.video_title, self.video_description, self.video_length)

    def __str__(self):
        return self.video_title