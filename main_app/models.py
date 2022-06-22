from django.db import models
from django.urls import reverse

# Create your models here.

DURATIONS = (
    ('A', 'One Week'),
    ('B', 'One Month'),
    ('C', 'Three Months')
)

class Bag(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    cost = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bag_id': self.id})

class Rentals(models.Model):
    date = models.DateField('Rental Start Date')
    duration = models.CharField(max_length=1, choices=DURATIONS, default=DURATIONS[0][0])
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Was rented for {self.get_duration_display()} on {self.date}"

    class Meta:
        ordering = ['date']