from django.db import models
from util.models import BaseModel
from django.contrib.auth import get_user_model

# Create your models here.

class UserProfile(BaseModel): 
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')

    def __str__(self) -> str:
        return self.user.username