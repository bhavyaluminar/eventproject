from django.db import models

# Create your models here.


from accounts.models import CustomUser
class Event(models.Model):
    title = models.CharField(max_length=30)

    description = models.TextField()

    date = models.DateField()
    # yyyy - mm - dd

    time = models.TimeField()
    # hh: mm:ss

    amount = models.IntegerField()

    venue = models.CharField(max_length=30)

    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    total_seats = models.IntegerField()

    available_seats = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)