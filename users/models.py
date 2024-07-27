from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,age,name,date_of_birth,phone_number,password= None,**extra_fields):
        if not email :
            raise ValueError("Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,age=age ,name=name,date_of_birth=date_of_birth,phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self,email,age,name,date_of_birth,phone_number,password= None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser = True. '))
        return self.create_user(email,age,name,date_of_birth,phone_number,password,**extra_fields)
    
class CustomUser(AbstractBaseUser):
    today = datetime.date.today()
    year = today.year
    
     
        
    age = models.PositiveIntegerField()
    name= models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['age', 'name', 'date_of_birth', 'phone_number']

    objects = CustomUserManager()

    def _str_(self):
        return self.age

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser