
from django.db import models

# Create your models here.

#def ExcelFile(models.Model):
#-------------------------------------------------------------------------------------------------------
class LabelName(models.Model):
	Preprocess = models.CharField(max_length = 1)
	Label = models.CharField(max_length = 100)
	split = models.IntegerField()
	test = models.CharField(max_length = 1)
	def __str__(self):
		return self.Label
 

#--------------------------------------------------------------------------------------------------------
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)


#---------------------------------------------------------------------------------------------------------



















