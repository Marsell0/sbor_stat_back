from django.db import models
from apps.criteria.models import Criteria
from apps.users.models import User

# Create your models here.
class Report(models.Model):
    RESULT_DONE = 'done'
    RESULT_PROCESS = 'process'
    REUSLT_PASSED = 'passed'
    RESULT_INWORK = 'in_work'
    RESULT_CHOICES = [
        (RESULT_DONE, 'выполнено'),
        (RESULT_PROCESS, 'в процессе'),
        (REUSLT_PASSED, 'сдано'),
        (RESULT_INWORK, 'в работе')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    about_event = models.TextField( default='mero')
    date = models.DateField(auto_now=True)
    members = models.TextField(default='member')
    result =  models.CharField(
        max_length=20,
        choices=RESULT_CHOICES,
        default=RESULT_PROCESS,
        help_text='Результаты'
    )
    proofs = models.TextField(blank=True)
    criteria = models.ManyToManyField(Criteria)
    checked_by_head = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)