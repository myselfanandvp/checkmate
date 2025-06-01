from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email: str, username: str, phonenumber: str, password: str, **extrafields: Any) -> Any:

        if not email:
            raise ValueError("Email is not provided")
        if not phonenumber:
            raise ValueError("Phonenumber is not provided")
        if not password:
            raise ValueError("Password is not provided")

        email = self.normalize_email(email)
        category = extrafields.get("category", "user")
        if category == "admin":
            extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_user", True)
        extrafields.setdefault("is_active", True)
        newuser = self.model(email=email, username=username,phonenumber=phonenumber, **extrafields)
        newuser.set_password(password)
        newuser.save(using=self._db)
        return newuser

    def create_superuser(self, email: str, username: str, phonenumber: str, password: str, **extrafields: Any) -> "User":
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("is_active", True)
        extrafields.setdefault('category',"superuser")            
        return self.create_user(email=email, username=username, password=password, phonenumber=phonenumber, **extrafields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=13, validators=[RegexValidator(
        r'^\+\d{12}$', 'Phone number must be exactly 12 digit starting with +91 sign')])
    profile_img = models.ImageField(
        upload_to='profile_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    CATEGORY_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
    ]
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default='user')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phonenumber', 'username','password']

    def __str__(self) -> str:
        return f"{self.email}"
