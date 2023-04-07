from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)
class User(AbstractUser):
    
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    has_posted = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    

class Hackathon(models.Model):
    TYPE = (
        ('image','image'),
        ('file','file'),
        ('link','link')
    )

    
    title = models.CharField(max_length=100,null=True) 
    description = models.CharField(max_length=500,null=True)
    hackathonImage = models.ImageField(upload_to='images')
    typeofSubmission = models.CharField(max_length=50,null=True, choices=TYPE)
    start = models.DateField()
    end = models.DateField()
    reward = models.CharField(max_length=100,null=True)
    participants = models.ManyToManyField(User,related_name="hackathon",blank=True)

    def __str__(self) :
        return self.title
    
class Submission(models.Model):
    name = models.CharField(max_length=50,null=True)
    summary = models.CharField(max_length=300,null=True)
    participant = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    hackathon = models.ForeignKey(Hackathon,null=True, on_delete=models.SET_NULL)
    fileSubmission = models.FileField(upload_to='hackathon/submissions/',null=True,validators=[FileExtensionValidator(['pdf'])]) #file submission
    imageSubmission = models.ImageField(upload_to='hackathon/submissions/images',null=True,validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'svg'])]) #file submission
    urlSubmission = models.URLField(null=True,validators=[URLValidator()])#link submission
                                                                     
