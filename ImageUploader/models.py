from django.db import models

# Create your models here.
class PrescriptionImage(models.Model):

    def nameFile(instance,filename):
         return '/'.join(['UserPrescriptionImage', str(instance.Username), filename])




    Username = models.CharField(max_length=50,)
    #UserId = models.IntegerField()
    image = models.ImageField(upload_to=nameFile, max_length=250)
    def __str__(self):
         return self.Username