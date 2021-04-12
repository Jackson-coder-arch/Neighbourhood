from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    photo = CloudianaryField('image')
    counts =models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='created_by')

    @classmethod
    def get_info(cls):
        info = cls.objects.all()
        return info

    class Meta:
        ordering = ["-pk"]

    @property
    def save_NeighbourHood(self):
        self.save()

    def delete_NeighbourHood(self):
        self.delete()

    @classmethod
    def search_NeighbourHood_by_name(cls, search_term):
        NeighbourHood = cls.objects.filter(name_icontains=search_term)
        return NeighbourHood



 

class User(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_photo = CloudianaryField('image')
    email = models.EmailField('email',unique=True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)



class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_created_by')

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email =self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(user=self.db)
        return user

    def create_superuser(self,email,username,password):
        user = self.model(
            email =self.normalize_email(email),
            password = password,
            username =username ,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60,unique=True)
    username = models.CharField(max_length=30, unique= True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username',]


    def __str__(self):   
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True 




    


