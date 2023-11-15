from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/')
    description = models.CharField(max_length=300)
    timeStart = models.CharField(max_length=50)
    timeEnd = models.CharField(max_length=50, blank=True)
    allDay = models.BooleanField()
    color = models.CharField(max_length=100)
    owner = models.ForeignKey(
        "users.User", related_name="events", on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.title