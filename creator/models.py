from django.db import models

# Create your models here.

class Meme(models.Model):
    name = models.CharField(max_length=100)
    background_file = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Macro(models.Model):
    top_text = models.CharField(max_length=1000)
    bottom_text = models.CharField(max_length=1000)
    imgur_id = models.CharField(max_length=20)
    meme = models.ForeignKey(Meme)

    def __unicode__(self):
        return u"{0}. {1}. {2}".format(self.meme.name, self.top_text, self.bottom_text)

