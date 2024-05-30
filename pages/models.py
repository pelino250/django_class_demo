from django.db import models


class ViewType(models.Model):
    short_name = models.CharField(max_length=50)  # short_name varchar(50)
    long_name = models.CharField(max_length=255)  # long_name varchar(255)

    def __str__(self):
        return self.short_name