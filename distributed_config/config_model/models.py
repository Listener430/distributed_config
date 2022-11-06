from django.db import models


class ValueName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class DictConfig(models.Model):
    system_name = models.CharField(max_length=200)
    value_names = models.ManyToManyField(ValueName, through='DictConfigValueName')
    version = models.PositiveIntegerField(null = True)
    in_use_indicator = models.CharField(max_length=20)


class DictConfigValueName(models.Model):
    value_name = models.ForeignKey(ValueName, on_delete=models.CASCADE)
    system_name = models.ForeignKey(DictConfig, on_delete=models.CASCADE)
