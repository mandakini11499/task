from django.db import models

class UserModel(models.Model):
    user_name=models.CharField(max_length=100,blank=False,null=False)
    user_email_id=models.EmailField()
    password=models.CharField(max_length=50,blank=False,null=False)


