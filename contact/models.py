from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    message = models.CharField(max_length=300)

