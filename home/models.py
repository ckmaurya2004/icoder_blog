from django.db import models

# Create your models here.
class Contact(models.Model):
    S_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=  100)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    desc = models.TextField(max_length=500)
    timestemp = models.DateField(auto_now_add=True,blank=True)

    def __str__(self) :
        return self.name
    
