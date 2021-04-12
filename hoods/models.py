from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cloudinary.models import CloudinaryField
# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    photo=CloudinaryField('image')
    counts =models.IntegerField()


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



 

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile', null = True)
    profile_photo = CloudinaryField('image')
    email = models.EmailField('email',unique=True)
    estate = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} User'

    def save_user(self):
        self.user

    def delete_user(self):
        self.delete()



class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    estate = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    business_photo = CloudinaryField('image')
    location = models.CharField(max_length=150)

    @classmethod
    def get_info(cls):
        info = cls.objects.all()
        return info

    class Meta:
        ordering = ["-pk"]

    @property
    def save_Business(self):
        self.save()

    def delete_Business(self):
        self.delete()



# class MyAccountManager(BaseUserManager):
#     def create_user(self,email,username,password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username")

#         user = self.model(
#             email =self.normalize_email(email),
#             username = username,
#         )

#         user.set_password(password)
#         user.save(user=self.db)
#         return user

#     def create_superuser(self,email,username,password):
#         user = self.model(
#             email =self.normalize_email(email),
#             password = password,
#             username =username ,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self.db)
#         return user

# class Account(AbstractBaseUser):
#     email = models.EmailField(max_length=60,unique=True)
#     username = models.CharField(max_length=30, unique= True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS =['username',]


#     def __str__(self):   
#         return self.email

#     def has_perm(self,perm,obj=None):
#         return self.is_admin

#     def has_module_perms(self,app_label):
#         return True 




    


