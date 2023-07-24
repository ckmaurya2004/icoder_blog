from django.db import models
from django.contrib.auth.models  import User 
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    S_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=  100)
    author = models.CharField(max_length=  100,default="")
    slug = models.CharField(max_length=  100)
    desc = models.TextField(max_length=5000)
    timestemp = models.DateField(blank=True)
    image = models.ImageField(upload_to = "blog/images",default="")

    def __str__(self) :
        return self.title
    

class BlogComment(models.Model):
    S_no = models.AutoField(primary_key=True)
    comments = models.TextField(max_length=500)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    post = models.ForeignKey(Post,on_delete= models.CASCADE)
    parent =models.ForeignKey('self',on_delete=models.CASCADE , null=True)
    timestemp = models.DateField(default=now)

    def __str__(self) :
        return  self.user.first_name 
     
    
