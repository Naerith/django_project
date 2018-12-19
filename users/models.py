from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #delete the profile with the user but not the user with deleting the profile.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #default is a default image for all users
    #when a user uploads a pic it saves it into profile_pics directory.

    def __str__(self):
        return f'{self.user.username} Profile'
