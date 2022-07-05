from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    is_public = models.BooleanField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Bag(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bagcat', null=True)
    name = models.CharField('Bag name', max_length=30)
    img = models.ImageField('Bag image', upload_to='media', null=True)
    about = models.TextField('Bag about', null=True)
    price = models.IntegerField('Bag price', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bag'
        verbose_name_plural = 'Bags'