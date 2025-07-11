from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Categories', max_length = 50)
    slug = models.SlugField(max_length= 50)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    cover_image = models.ImageField(upload_to= 'img', blank=True, null = True)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to= 'pdf')
    recommended_books = models.BooleanField(default=False)
    fiction_books = models.BooleanField(default=False)
    business_books = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
