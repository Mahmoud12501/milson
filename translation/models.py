from django.db import models
from django.utils.text import slugify

# help func


class TranslateDb(models.Model):
    t_from=models.ForeignKey('Languges',verbose_name='Translation from',related_name='trsn_from',on_delete=models.CASCADE)
    t_to=models.ForeignKey('Languges',verbose_name='Translation to',related_name='trsn_to',on_delete=models.CASCADE)
    file=models.FileField('file',upload_to='files/')
    word_count=models.IntegerField('word_count')
    phone=models.CharField(max_length=15,null=True,blank=True,unique=True)
    email=models.EmailField(null=True,blank=True)
    creat_at=models.DateField(auto_now=True)

    def __str__(self):
        if self.email=='':
            return str(self.phone)
        else:
            return str(self.email)

class Languges(models.Model):
    languge=models.CharField(max_length=40)
    slug=models.SlugField(max_length=40,blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.languge) 
        super(Languges,self).save(*args,**kwargs)
    
    def __str__(self):
        
        return str(self.languge)