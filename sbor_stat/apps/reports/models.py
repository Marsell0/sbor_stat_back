from django.db import models
from apps.criteria.models import Criteria
from apps.users.models import User

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    criteria = models.ManyToManyField(Criteria)
    checked_by_head = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)