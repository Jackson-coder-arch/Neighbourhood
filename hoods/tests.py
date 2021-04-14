from django.test import TestCase
from .models import *

class NeighbourHoodTestClass(TestCase):
    def setUp(self):
        self.NeighbourHood = NeighbourHood(name='Yes', location='Nairobi',
        image='default.png', 
        counts='0',)
        self.NeighbourHood.save_NeighbourHood()
 
    def test_create_hood(self):
        self.NeighbourHood.save_NeighbourHood()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_NeighbouHood(self):
        self.NeighbourHood.save_NeighbourHood()
        self.NeighbourHood.delete_NeighbourHood()
        neighbourhoods = NeighbourHood.objects.all() v
        neighbourhood = NeighbourHood.search_hood('test')
        self.assertTrue(len(hoods) <= 0)

    def test_update_NeighbourHood(self):
        self.NeighbourHood.save_NeighbourHood()

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Yes',
        description='description',
        business_photo='default.png',
        location='kikuyu' 
        description='we love business',)
        self.business.create_business()

    def test_delete_business(self):
        self.business.create_business()
        self.business.delete_business()
        posts = Business.objects.all()
        self.assertTrue(len(posts) <= 0)
    def search_business(self):
        self.business.create_business()
        post = Business.find_business(business_id)
        self.assertEqual(post.id,'1')

class ProfileTestClass(TestCase):
    from django.contrib.auth.models import User
    def setUp(self):
        self.user = User(username='jack')
        self.user.save()
        self.profile = Profile(profile_picture='default.png',bio='Am Ikonya ', name='person')
        self.profile.save_profile()
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Hood.objects.all().delete()
        Business.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile, Profile))
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)