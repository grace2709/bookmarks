from django.db import models
from django.conf import settings
from django.conf.urls.static import static
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null =True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/",blank=True)




    def __str__(self):
        return f'profile for user {self.user.username}'