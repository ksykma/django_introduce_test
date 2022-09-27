from django.db import models



class AccessLog(models.Model):
    created_at = models.DateTimeField("접속시간", auto_now_add=True)
    location = models.CharField("접속경로", max_length=50)
    
    def __str__(self):
        return f"{self.created_at} / {self.location}"