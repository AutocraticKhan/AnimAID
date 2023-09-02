from django.db import models

class Animation(models.Model):
    MODE_CHOICES = [
        ('Mode_1', 'Center character'),
        ('Mode_2', 'Side character'),
        ('Mode_3', 'Only Background'),
    ]
    
    CHARACTER_CHOICES = [
        ('Character Main', 'Character Main'),
        ('Character_2', 'Character 2'),
        ('Character_3', 'Character 3'),
    ]
    
    DIR_CHOICES = [
        ('L', 'Left'),
        ('R', 'Right'),
        ('M', 'Middle'),
    ]

    EMOTION_CHOICES = [
        ('Happy', 'Happy'),
        ('Sad', 'Sad'),
        ('Angry', 'Angry'),
        ('Neutral', 'Neutral'),
    ]

    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    character = models.CharField(max_length=15, choices=CHARACTER_CHOICES)
    dir_head = models.CharField(max_length=1, choices=DIR_CHOICES)
    emotion = models.CharField(max_length=10, choices=EMOTION_CHOICES)
    dir_eye = models.CharField(max_length=1, choices=DIR_CHOICES)
    word = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    foreground = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.mode} - {self.character}"
