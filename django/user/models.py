""" user part"""
from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):

    def create_user(self, 
                    first_name:str, 
                    last_name:str,
                    email:str, 
                    password:str = None,
                    is_staff = False,
                    is_superuser = False,
                    ) -> "User":

        if not email: 
            raise ValueError("Must input email")        
        if not first_name: 
            raise ValueError("Must input first name")        
        if not last_name: 
            raise ValueError("Must input last name")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, 
                    first_name:str, 
                    last_name:str,
                    email:str, 
                    password:str = None,
                    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name, 
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=100,null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=100,null=True)
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True, null=True)
    password = models.CharField(max_length=100)
    date_creation = models.DateTimeField(null=False,blank=True,auto_now_add=True)
    
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]
