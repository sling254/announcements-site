from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,verbose_name='email address')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()



class Priest(models.Model):
    Rank=(
        ("Diocesan","Diocesan"),
        ("Missionary","Missionary"),
    )
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    rank = models.CharField(choices=Rank, max_length=50)
    date_of_birth = models.DateField(verbose_name='date_of_birth')
    place_of_birth = models.CharField(max_length=255)

    def __str__(self):
        return self.email
class Parishioner(models.Model):
    church_gruop=(
        ("CMA","CMA"),
        ("CWA","CWA"),
    
    )
        
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    jumuia = models.CharField(max_length=200)
    church_gruop = models.CharField(choices=church_gruop,max_length=50)
