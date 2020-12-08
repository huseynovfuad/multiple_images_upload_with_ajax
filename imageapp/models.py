from django.db import models

# Create your models here.



def upload_to(instance,filename):
    return '%s/%s/%s'%('image',instance.pk,filename)
    

class ImageModel(models.Model):
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return "image {}".format(self.id)
