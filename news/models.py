from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Почты'

class Town(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    coord = models.CharField(max_length=100)
    def publish(self):
        print('Coord Town' + self.name + ' ' + self.coord)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class zakaz(models.Model):
    YouTown = models.ForeignKey(Town, on_delete=models.CASCADE)
    ArrivalTown = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='topic_content_type')
    Nick_Recipient = models.CharField(max_length=200)
    You_Nick = models.CharField(max_length = 200)
    def __str__(self):
        return self.You_Nick
