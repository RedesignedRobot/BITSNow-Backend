import datetime

from django.db import models

class Items(models.Model):
    eTitle = models.CharField(max_length=255, default='')
    eDesc = models.CharField(max_length=255, default='')
    cName = models.CharField(max_length=255, default='')
    cId = models.CharField(max_length=255, default='')
    eStartDate = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now(), blank=True)
    eEndDate = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now(), blank=True)


    def __str__(self):
        return "{}".format(self.eTitle)