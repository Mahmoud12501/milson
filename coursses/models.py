from django.db import models
from django.utils.text import slugify

# Create your models here.
class Coursse(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=800)
    price=models.FloatField()
    image=models.ImageField(upload_to="coursses/")
    slug=models.SlugField(max_length=40,blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name) 
        super(Coursse,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.name