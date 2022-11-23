from django.db import models
from django.core.validators import RegexValidator

class ComplainRecord(models.Model):

    # error message when a wrong format entered
    phone_message = 'Phone number must be entered in the format: 05999999999' 

     # your desired format 
    phone_regex = RegexValidator(
        regex=r'^(05)\d{9}$',
        message=phone_message
    )

    complain_number = models.IntegerField()
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    mobile_number = models.CharField(validators=[phone_regex], max_length=60, null=True, blank=True)
    Description = models.CharField(max_length=1000)
    date_time = models.DateTimeField()
    Resolved = models.BooleanField()
    
