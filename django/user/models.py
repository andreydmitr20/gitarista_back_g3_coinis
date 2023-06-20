""" user part"""
from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):

    def create_user(self, 
                    username:str,
                    email:str, 
                    password:str = None,
                    is_staff = False,
                    is_superuser = False,
                    ) -> "Users":

        if not email: 
            raise ValueError("Must input email")          
        if not username: 
            raise ValueError("Must input username")        

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, 
                    username:str,
                    email:str, 
                    password:str = None,
                    ) -> "Users":
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user

class Users(auth_models.AbstractUser):
    user_id = models.BigAutoField(primary_key=True, db_column='user_id')
    email = models.EmailField(verbose_name="email", max_length=100, unique=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    date_creation = models.DateTimeField(null=False,blank=True,auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return str(self.username)+(' - ')+str(self.email)
