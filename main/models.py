from django.db import models


class Command(models.Model):
    cmd = models.TextField(null = True)
