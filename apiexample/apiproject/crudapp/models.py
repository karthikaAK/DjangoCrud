from django.db import models


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    roll_num = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"