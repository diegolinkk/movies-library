from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20,)

    class Meta:
        verbose_name_plural = "Categories" #indica o nome correto do plural no admin
    
    def __str__(self): #lista de forma mais natural a propriedade do objeto nas listas
        return self.category_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    publish_date = models.DateField()
    category = models.ForeignKey(Category, on_delete = models.SET_NULL,null=True)

    def __str__(self):
        return self.movie_name