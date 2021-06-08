from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.

class myUserManager(BaseUserManager):
    
    def create_user(self,email,password=None):
        "this function helps create a MyUser Instance"

        email = self.normalize_email(email)

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password=None):
        'create superuser -> help to create user that have admin access'
        user = self.create_user(email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()


        return user



class myUser(PermissionsMixin,AbstractBaseUser):
    "this is the custom user model that the whole application will be using instead of django defualt! "
    email = models.EmailField(unique=True)
    # name = models.CharField(max_length=100)
    is_active =  models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=False)

    objects = myUserManager()
    USERNAME_FIELD = 'email'


    def __str__ (self):
        return self.email
    