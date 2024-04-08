from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=30, verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=11, verbose_name='Phone Number')
    date = models.DateField(verbose_name='Reservation Date', auto_now=False, auto_now_add=False)
    time = models.TimeField(verbose_name='Reservation Time', auto_now=False, auto_now_add=False)
    number = models.PositiveSmallIntegerField(verbose_name='Number of Guests')

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

