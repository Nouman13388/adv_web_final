from django.db import models
from django.contrib.auth.models import User


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('lecture', 'Lecture'),
        ('assignment', 'Assignment'),
        ('reference', 'Reference'),
    ]
    
    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    description = models.TextField()
    uploaded_file = models.FileField(upload_to='resources/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
