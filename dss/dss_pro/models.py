from django.db import models

# Create your models here.
#created 3 models Documents , Folders , Topics
class Documents(models.Model):
    Documents= models.FileField(upload_to='Customer Feedback/',null=True, max_length=200)

class Folders(models.Model):
    Folders=models.FilePathField(path="Customer Feedback/", match="SpekiLove!")

class Topics(models.Model):
    Topics=models.CharField(max_length=225,blank=False)

    def __str__(self):
        return self.Topics