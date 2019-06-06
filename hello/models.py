from django.db import models

# Create your models here.
class Post(models.Model):  #掲示板本体のデータベース マイグレーションした  主モデル
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.title





