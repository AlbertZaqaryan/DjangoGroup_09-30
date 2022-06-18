from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('Category image', upload_to='media', null=True)
    about = models.TextField('Category about', null=True)
    price = models.IntegerField('Category price', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'