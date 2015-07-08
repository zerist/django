from django.db import models

# Create your models here.
class Word(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        super(Word, self).save(*args, **kwargs)
