from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
# help func


class TranslateDb(models.Model):
    t_from=models.ForeignKey('Languges',verbose_name='Translation from',related_name='trsn_from',on_delete=models.CASCADE)
    t_to=models.ForeignKey('Languges',verbose_name='Translation to',related_name='trsn_to',on_delete=models.CASCADE)
    file=models.FileField('file',upload_to='files/')
    word_count=models.IntegerField('word_count')
    phone=models.CharField(max_length=15,null=True,blank=True)
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
    
    
from django.core.mail import EmailMessage
@receiver(post_save,sender=TranslateDb)   
def create_profile(sender,instance,created,**kwargs):
    if created:
        
       
        trans=TranslateDb.objects.last()
        message=f"Dear transltor somone want translte this   file from {trans.t_from}  to {trans.t_to}  \n email: { trans.email}\n phone: {trans.phone}"
        send_mail(
                "translt job",
                 message,
                trans.email,
                [settings.EMAIL_HOST_USER]  
                
            )
        