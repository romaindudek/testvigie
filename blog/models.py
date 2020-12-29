from django.db import models

# Create your models here.
class TestBlog(models.Model):
    test_content = models.CharField('Description du besoin',max_length=250)