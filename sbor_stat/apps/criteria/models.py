from django.db import models


class CriteriaGroup(models.Model):
    """ Таблица для взаимоисключающих критериев """
    name = models.TextField(unique=True)


class Criteria(models.Model):
    name = models.CharField()
    point = models.DecimalField(max_digits=3, decimal_places=2)
    group = models.ForeignKey(CriteriaGroup, on_delete=models.CASCADE, null=True, blank=True)