from django.db import models

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
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
    email = models.EmailField('email'unique=True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)



class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_created_by')




    


