from django.db import models
from django.utils import timezone
from account.models import User


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)  # 영화명
    description = models.TextField()  # 영화설명
    poster = models.ImageField(upload_to='media/', blank=True, null=True)  # 포스터
    pub_date = models.DateField()  # 개봉일
    director = models.CharField(max_length=100)  # 감독
    create_date = models.DateTimeField(default=timezone.now)
    running_time = models.PositiveIntegerField(default=0)
    age_limit = models.CharField(max_length=15, default='전체관람가')

    def __str__(self):
        return self.title


class Pick(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    pick_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.nickname + " likes " + self.movie.title