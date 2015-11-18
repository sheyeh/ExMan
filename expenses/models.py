from django.conf import settings
from django.db import models
from users.models import Account

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=12,
                                 decimal_places=2)
    details = models.TextField()
    account = models.ForeignKey(Account)

    def __str__(self):
        return str(self.user) + " Expense #" + str(self.pk)