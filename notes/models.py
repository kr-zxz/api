from django.db import models
from django.contrib.auth.models import User



class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    cgpa = models.IntegerField()  # Change to IntegerField
    sslc_percentage = models.IntegerField()  # Change to IntegerField
    plus_two_percentage = models.IntegerField() 
    phone_number = models.CharField(max_length=15)  # Assuming phone number is stored as a string
    address = models.TextField()
    image = models.FileField(upload_to='user_files/', null=True, blank=True)  

    def __str__(self) :
        return (self.first_name)

    
