from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

TYPE_CHOICES = (
    (1, "STRONG"),
    (2, "POSSIBLE"),
    (3, "WEAK"),
    
)

# class TimeStampedModel(models.Model):
#     date_created = models.DateTimeField(blank=True, null=True)
#     last_updated = models.DateTimeField(blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if self.date_created is None:
#             self.date_created = timezone.now()
#         self.last_updated = timezone.now()
#         super().save(*args, **kwargs)

#     class Meta:
#         abstract = True


class ClientInfo(models.Model):
    first_name = models.CharField(max_length=100, help_text="type first name")
    last_name = models.CharField(max_length=100, help_text="type last name")
    province = models.CharField(max_length=2, help_text="province like ON, AB", blank=True)
    dat_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True


class Notice(ClientInfo):
    alt_first_name = models.CharField(max_length=100, help_text="alt first name", blank=True)
    alt_last_name = models.CharField(max_length=100, help_text="alt last name", blank=True)

    def __str__(self):
        return '{} by {}'.format(self.first_name, self.alt_first_name)

 
class Record(ClientInfo):
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Match(models.Model):
    record = models.ForeignKey(Record, on_delete=CASCADE)
    notice = models.ForeignKey(Notice, on_delete=CASCADE)
    type = models.PositiveIntegerField(choices=TYPE_CHOICES, default=1)



