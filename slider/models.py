from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    content = models.TextField()
    href = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='slider')

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'
        ordering = ['id']