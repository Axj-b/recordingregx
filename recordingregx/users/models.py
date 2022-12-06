from django.db import models
from django.contrib.auth.models import User

from PIL import Image



class Profile(models.Model):
    
    user = models.OneToOneField(User,related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    activated = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs) # calls the save method from parent class
        # no image needed here        
        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

    # class Meta:
    #     db_table="users_profile"