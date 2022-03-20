import random

from django.db import models


def pass_generator():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbol = '[]{}()!@#$%&*_+/*-'

    all = lower + upper + numbers + symbol
    lenght = 16
    password = "".join(random.sample(all, lenght))
    return password


class User(models.Model):
    username = models.CharField(
        max_length=20,
        blank=False)

    password = models.CharField(
        default=pass_generator(),
        max_length=16,
        blank=False,
        help_text='if blank, a random password will be generated.')

    birthdate = models.DateField(
        blank=False,
        max_length=10)
