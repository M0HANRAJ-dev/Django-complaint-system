from django.db import models

class Complaint(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=20,default='Normal')

    def __str__(self):
        return self.title
    
def auto_tag(description):
        urgent_keywords = ["fire","accident","voilence"]
        description = description.lower()
        for word in urgent_keywords:
            if word in description:
                return 'Urgent'
        return 'Normal'