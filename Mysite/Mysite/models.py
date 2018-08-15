from django.db import models
from django.template.defaultfilters import truncatechars
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify

#creates table Article
class Article(models.Model): #database
    id=models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30, verbose_name='Contents')
    content = RichTextField(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        super(Article,self).save()

    def __str__(self):
        return '%s' % self.title



#creating table Language
class Language(models.Model): #database
    id=models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, verbose_name='Language') 
    content = RichTextField(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        super(Language,self).save()

    def __str__(self):
        return '%s' % self.title



    
     
    
    
