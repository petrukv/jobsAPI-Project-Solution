from django.db import models

# Create your models here.

class JobOffers(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    salary = models.FloatField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.job_title} {self.company_name} {self.salary}'