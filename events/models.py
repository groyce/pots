from django.db import models
from django.urls import reverse


class Event(models.Model):
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    event_title = models.TextField('Event Title', blank='Event', null=False)
    description = models.TextField('Description', blank=True, null=True)
    location = models.TextField('Location', blank=True, null=True)

    class Meta:
        ordering = ('start_time',)

    def __str__(self):
        return self.event_title

    def get_absolute_url(self):
        return reverse('events:event_detail', args=[self.id])
