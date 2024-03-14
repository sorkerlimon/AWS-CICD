from django.db import models
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from shortuuidfield import ShortUUIDField 


class ApplyForm(models.Model):

    INTERESTED_FOR_CHOICES = [('Work From Home (WFH)', 'Work From Home (WFH)'),
                              ('Work From Office (WFO)', 'Work From Office (WFO)'),
                              ]
    
    WANT_TO_WORK_CHOICES = [('Morning (7 am - 3 pm)', 'Morning (7 am - 3 pm)'),
                            ('Evening (3 pm - 11 pm)', 'Evening (3 pm - 11 pm)'),
                            ('Night (11 pm - 7 am)', 'Night (11 pm - 7 am)'),
                            
                            ]
    HIGHEST_EDUCATIONS = [('Completed 10 years school', 'Completed 10 years school'),
                          ('University Degree', 'University Degree'),
                          ('University Degree - Masters', 'University Degree - Masters'),
                          ('Technical Degree', 'Technical Degree'),
                          ('Others', 'Others'), 
                            ]
    applicant_id = ShortUUIDField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    interested_for = models.CharField(max_length=50, choices=INTERESTED_FOR_CHOICES, default='Work From Home (WFH)')
    email = models.EmailField()

    phonenumber = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    want_to_work = models.CharField(max_length=50, choices=WANT_TO_WORK_CHOICES, default='Morning (7 am - 3 pm)')
    highest_education = models.CharField(max_length=100,choices=HIGHEST_EDUCATIONS,default='Completed 10 years school')
    country = CountryField(default='BD',null=True,blank=False)
    earliest_start_date = models.DateField()
    national_id = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    
    cv = models.FileField(upload_to='temp_cv/')
    profile_picture = models.ImageField(upload_to='Temp_pictures/', null=True, blank=True)
    meeting_link_sent = models.BooleanField(default=False)
    account_create = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}'s Profile"
