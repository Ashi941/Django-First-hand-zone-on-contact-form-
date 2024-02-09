from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length = 30,null = False, blank = False)
    email = models.EmailField(null = False, blank = False,unique = True)
    mobile = models.CharField(max_length = 12,null = True, blank = True)
    message = models.TextField(null = True, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
