from django.db import models

# Create your models here.
import datetime
import os

def get_file_path(request,filename):
    original_filename = filename 
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime, original_filename)
    return  os.path.join('upload/',filename)
class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name =  models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status =models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")

    def _str_(self):
        return self.name

class Product (models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=150,null=False,blank=False)
    name =  models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.CharField(max_length=250,null=False,blank=False)
    status =models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
 
    
    def _str_(self):
          return self.name
