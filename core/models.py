from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('list_of_book_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='book/pdfs/')
    cover = models.ImageField(upload_to='book/covers/', null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    views = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
