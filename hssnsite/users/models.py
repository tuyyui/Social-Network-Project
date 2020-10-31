from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date
from django.conf import settings

#Importing image
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    ethnic_choices = (("SOMALI", "SOMALI"), ("IRAN", "IRAN"),
                      ("SWAHILI", "SWAHILI"), ("EGYPTIAN", "EGYPTIAN"), ("INDONESIAN", "INDONESIAN"),
                      ("TURKISH", "TURKISH"), ("ETHIOPIAN", "ETHIOPIAN"))
    ethnic = models.CharField(max_length=20, choices=ethnic_choices, default="SOMALI")
    date_of_birth = models.DateField(default=date.today)
    family_size = models.CharField(max_length=2, default="")
    connections = models.ManyToManyField("Profile", blank=True)



    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        #overriding Save method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
#This code adds users with similar ethnicities and family sizes to their connections (or this can be called a friend list)


#class Connect(models.Model):
 #   to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user')
  #  from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user')
   # timestamp = models.DateTimeField(auto_now_add=True) #This tells when the stamp was created

    #def __str__(self):
     #   return "from {}, to {}".format(self.from_user.username, self.to_user.username)











