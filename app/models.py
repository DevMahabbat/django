from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="Mətn")
    explanation = models.TextField(verbose_name="İzah")
    author = models.ForeignKey(to="auth.User" ,on_delete= models.CASCADE,verbose_name='Yazıçı')
    