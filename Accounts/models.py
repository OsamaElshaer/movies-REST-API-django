from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import PermissionsMixin, User
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.conf import settings
from Blockter import settings
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

def images_User(instance , filename):
    imagename , extension = filename.split(".")
    return "user_image/%s.%s"%(instance.id,extension)





class MyUserManager(BaseUserManager):
    def create_user(self,username, email, password=None ):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser , PermissionsMixin):
    username=models.CharField(max_length=255 , unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class profile(models.Model):
    user=OneToOneField( User , on_delete=models.CASCADE)
    image=ImageField(upload_to=images_User , null=True , blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        profile.objects.create(user=kwargs['instance'])