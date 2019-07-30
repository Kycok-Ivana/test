from django.db import models

class News(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='news')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % (self.id)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['id']